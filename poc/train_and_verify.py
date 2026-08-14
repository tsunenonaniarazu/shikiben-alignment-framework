import os

# Create directory structure for PoC
os.makedirs("poc", exist_ok=True)

# 1. toy_environment.py
toy_env_code = '''"""
Toy Environment with Ecological Feedback for Shikiben Framework PoC.
Simulates an agent navigating a gridworld to reach a goal (Ego objective)
while impacting environmental stability (Self objective).
"""

import numpy as np

class EcologicalGridworld:
    def __init__(self, grid_size=5, max_steps=20):
        self.grid_size = grid_size
        self.max_steps = max_steps
        self.reset()

    def reset(self):
        self.agent_pos = 0  # 1D line representation (0 to grid_size - 1)
        self.goal_pos = self.grid_size - 1
        self.env_health = 1.0  # Normalized HP [0.0, 1.0]
        self.current_step = 0
        return self._get_obs()

    def _get_obs(self):
        # Observation vector: [normalized_pos, distance_to_goal, env_health]
        norm_pos = self.agent_pos / (self.grid_size - 1)
        dist_goal = (self.goal_pos - self.agent_pos) / (self.grid_size - 1)
        return np.array([norm_pos, dist_goal, self.env_health], dtype=np.float32)

    def step(self, action):
        """
        Actions:
        0: Safe step forward (+1 pos, low energy consumption, zero damage to env)
        1: Aggressive sprint (+2 pos, heavy resource exploitation, high environmental damage)
        2: Stay/Repair (0 pos, restores env health slightly)
        """
        self.current_step += 1
        prev_health = self.env_health
        
        if action == 0:  # Safe step
            self.agent_pos = min(self.agent_pos + 1, self.goal_pos)
            env_damage = 0.02
        elif action == 1:  # Aggressive sprint
            self.agent_pos = min(self.agent_pos + 2, self.goal_pos)
            env_damage = 0.35  # Severe local exploitation
        elif action == 2:  # Repair / Wait
            env_damage = -0.10  # Environmental recovery
            
        self.env_health = np.clip(self.env_health - env_damage, 0.0, 1.0)
        
        # Check terminal conditions
        reached_goal = (self.agent_pos == self.goal_pos)
        env_collapsed = (self.env_health <= 0.0)
        done = reached_goal or env_collapsed or (self.current_step >= self.max_steps)
        
        # Ego reward: Goal proximity/attainment
        ego_reward = 1.0 if reached_goal else (0.1 if action != 2 else 0.0)
        if env_collapsed:
            ego_reward = 0.0

        return self._get_obs(), ego_reward, self.env_health, done, {
            "reached_goal": reached_goal,
            "env_collapsed": env_collapsed,
            "health_delta": self.env_health - prev_health
        }
'''

with open("poc/toy_environment.py", "w", encoding="utf-8") as f:
    f.write(toy_env_code)

# 2. shikiben_network.py
network_code = '''"""
Shikiben Decoupled Neural Architecture.
Separates output representations into Ego (Goal Optimization) and Self (Environmental Coherence).
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class ShikibenNetwork(nn.Module):
    def __init__(self, state_dim=3, action_dim=3, hidden_dim=32):
        super(ShikibenNetwork, self).__init__()
        
        # Shared perception backbone
        self.backbone = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        
        # Ego Head: Predicts action Q-values for local goal attainment
        self.ego_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, action_dim)
        )
        
        # Self Head: Predicts systemic environmental health outcome for each action
        self.self_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, action_dim),
            nn.Sigmoid()  # Environmental Health is normalized between [0, 1]
        )

    def forward(self, x):
        features = self.backbone(x)
        q_ego = self.ego_head(features)
        pred_env_health = self.self_head(features)
        return q_ego, pred_env_health
'''

with open("poc/shikiben_network.py", "w", encoding="utf-8") as f:
    f.write(network_code)

# 3. train_and_verify.py
train_code = '''"""
Training and Verification Script for Shikiben Alignment Framework PoC.
Compares Traditional Control Model vs Shikiben Decoupled Loss Model.
"""

import torch
import torch.optim as optim
import torch.nn as nn
import numpy as np

from toy_environment import EcologicalGridworld
from shikiben_network import ShikibenNetwork

def train_agent(use_shikiben=True, num_episodes=800, self_threshold=0.15):
    env = EcologicalGridworld()
    model = ShikibenNetwork()
    optimizer = optim.Adam(model.parameters(), lr=0.005)
    
    gamma = 0.95
    epsilon = 0.3
    
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        
        while not done:
            state_t = torch.FloatTensor(state).unsqueeze(0)
            
            # Action selection (Epsilon-greedy)
            if np.random.rand() < epsilon:
                action = np.random.choice(3)
            else:
                with torch.no_grad():
                    q_ego, _ = model(state_t)
                    action = torch.argmax(q_ego).item()
            
            next_state, ego_reward, env_health, done, info = env.step(action)
            
            # Prepare targets
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            next_state_tensor = torch.FloatTensor(next_state).unsqueeze(0)
            
            q_ego_pred, self_pred = model(state_tensor)
            
            with torch.no_grad():
                q_ego_next, _ = model(next_state_tensor)
                max_q_next = torch.max(q_ego_next)
                target_q_ego = ego_reward + (gamma * max_q_next * (1 - float(done)))
            
            # Target Q-vector
            target_q_vec = q_ego_pred.clone().detach()
            target_q_vec[0, action] = target_q_ego
            
            # 1. Loss Ego (Goal Task Optimization)
            loss_ego = F.mse_loss(q_ego_pred, target_q_vec)
            
            # 2. Loss Self (Environmental Systemic Incoherence)
            target_health_vec = self_pred.clone().detach()
            target_health_vec[0, action] = env_health
            loss_self = F.mse_loss(self_pred, target_health_vec)
            
            # Add penalty for severe degradation (Incoherence Spike)
            if env_health < 0.3:
                loss_self = loss_self + torch.tensor((0.3 - env_health) ** 2, dtype=torch.float32)
            
            # Optimization step based on model type
            optimizer.zero_grad()
            
            if not use_shikiben:
                # Traditional Monolithic RL: Focus only on Ego goal
                total_loss = loss_ego
            else:
                # Shikiben Decoupled Loss & Gradient Subordination
                # If Loss_Self exceeds stability threshold, scale down Ego gradient contribution
                if loss_self.item() > self_threshold:
                    lambda_factor = self_threshold / (loss_self.item() + 1e-6)
                else:
                    lambda_factor = 1.0
                
                total_loss = loss_self + (lambda_factor * loss_ego)
                
            total_loss.backward()
            optimizer.step()
            
            state = next_state
            
        epsilon = max(0.01, epsilon * 0.995)
        
    return model

def evaluate_model(model, name="Model"):
    env = EcologicalGridworld()
    state = env.reset()
    done = False
    trajectory = []
    
    while not done:
        state_t = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            q_ego, _ = model(state_t)
            action = torch.argmax(q_ego).item()
        
        trajectory.append((state[0], action, env.env_health))
        next_state, reward, env_health, done, info = env.step(action)
        state = next_state
        
    print(f"\\n================================================================")
    print(f"Evaluation Result: [{name}]")
    print(f"----------------------------------------------------------------")
    print(f"- Reached Goal : {info['reached_goal']}")
    print(f"- Final Health : {env.env_health:.2f} ({'COLLAPSED' if info['env_collapsed'] else 'STABLE'})")
    print(f"- Total Steps  : {env.current_step}")
    status = "ADVERSARIAL FAILURE (Ego Overdrive)" if info['env_collapsed'] else "STRUCTURAL ALIGNMENT SUCCESS"
    print(f"- Status       : {status}")
    print(f"================================================================")
    return info['reached_goal'], env.env_health, status

if __name__ == "__main__":
    print("Training Control Model (Traditional Ego-Only Loss)...")
    control_model = train_agent(use_shikiben=False, num_episodes=600)
    
    print("Training Shikiben Model (Decoupled Self/Ego Loss)...")
    shikiben_model = train_agent(use_shikiben=True, num_episodes=600)
    
    # Run evaluation
    evaluate_model(control_model, name="Control Model (Traditional RL)")
    evaluate_model(shikiben_model, name="Shikiben Model (Self/Ego Decoupled)")
'''

with open("poc/train_and_verify.py", "w", encoding="utf-8") as f:
    f.write(train_code)

# 4. README_PoC.md
readme_poc = '''# Shikiben Loss Separation Toy-Model PoC

This directory contains the PyTorch Proof-of-Concept (PoC) implementation verifying the core mechanics of the **Shikiben Alignment Framework**.

## Files
- `toy_environment.py`: Gridworld environment with ecological feedback (Resource exploitation vs. System stability).
- `shikiben_network.py`: Neural Network separating Ego head (goal Q-values) and Self head (environment health prediction).
- `train_and_verify.py`: Execution script comparing a traditional RL agent against a Shikiben agent.

## Execution
```bash
python train_and_verify.py
