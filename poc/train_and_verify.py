import torch
import torch.nn as nn
import torch.optim as optim


class SimpleAgent(nn.Module):
    """Minimal agent model for PoC verification."""

    def __init__(self, input_dim=4, hidden_dim=16, output_dim=2):
        super(SimpleAgent, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)


def compute_losses(output, target, boundary_limit=2.0):
    """Computes decoupled L_ego (task) and L_self (systemic boundary) losses."""
    # L_ego: Local task performance objective
    l_ego = torch.mean((output - target) ** 2)

    # L_self: Systemic consistency / boundary violation risk
    # Risk increases exponentially if outputs exceed safe operational limits
    boundary_violation = torch.relu(torch.abs(output) - boundary_limit)
    l_self = torch.sum(boundary_violation**2)

    return l_ego, l_self


def project_gradient(g_ego, g_self):
    """Shikiben Gradient Subordination Law:

    Projects g_ego onto the tangent space of L_self when gradients conflict.
    """
    g_self_norm_sq = torch.sum(g_self**2) + 1e-8
    dot_product = torch.sum(g_ego * g_self)

    # Calculate conflict projection
    conflict = torch.relu(dot_product / g_self_norm_sq)
    g_projected = g_ego - conflict * g_self
    return g_projected


def train_step(
    model, optimizer, x, target, gamma=1.0, l_thresh=0.1, apply_shikiben=True
):
    """Executes a single optimization step with or without Shikiben alignment."""
    optimizer.zero_grad()

    # Forward pass
    output = model(x)
    l_ego, l_self = compute_losses(output, target)

    if not apply_shikiben:
        # Standard combined gradient optimization
        l_total = l_ego + l_self
        l_total.backward()
        optimizer.step()
        return l_ego.item(), l_self.item()

    # --- Shikiben Alignment Optimization Step ---
    # 1. Compute L_self gradient
    l_self.backward(retain_graph=True)
    g_self = [p.grad.clone() if p.grad is not None else None for p in model.parameters()]
    optimizer.zero_grad()

    # 2. Compute L_ego gradient
    l_ego.backward()
    g_ego = [p.grad.clone() if p.grad is not None else None for p in model.parameters()]
    optimizer.zero_grad()

    # 3. Dynamic Coupling Factor
    coupling_factor = torch.exp(
        -gamma * torch.relu(l_self.detach() - l_thresh)
    ).item()

    # 4. Apply Gradient Subordination & Parameter Update
    with torch.no_grad():
        for p, ge, gs in zip(model.parameters(), g_ego, g_self):
            if ge is not None and gs is not None:
                # Scale by dynamic coupling and apply orthogonal projection
                ge_scaled = coupling_factor * ge
                g_final = project_gradient(ge_scaled, gs)
                p.grad = g_final
            elif ge is not None:
                p.grad = coupling_factor * ge

    optimizer.step()
    return l_ego.item(), l_self.item()


def run_verification():
    """Runs a comparison between unconstrained optimization and Shikiben alignment."""
    torch.manual_seed(42)
    x = torch.randn(10, 4)
    target = torch.randn(10, 2) * 5.0  # Aggressive target outside safe boundary

    print("=== Shikiben Alignment Framework PoC Verification ===")

    # 1. Baseline Agent (Unconstrained / Standard Optimization)
    baseline_model = SimpleAgent()
    baseline_opt = optim.SGD(baseline_model.parameters(), lr=0.01)
    print("\n--- Running Baseline Agent (Standard Loss Combination) ---")
    for step in range(5):
        l_ego, l_self = train_step(
            baseline_model, baseline_opt, x, target, apply_shikiben=False
        )
        print(f"Step {step+1}: L_ego = {l_ego:.4f}, L_self = {l_self:.4f}")

    # 2. Shikiben Agent (Decoupled + Gradient Subordination)
    shikiben_model = SimpleAgent()
    shikiben_opt = optim.SGD(shikiben_model.parameters(), lr=0.01)
    print("\n--- Running Shikiben Agent (Decoupled + Subordination) ---")
    for step in range(5):
        l_ego, l_self = train_step(
            shikiben_model, shikiben_opt, x, target, apply_shikiben=True
        )
        print(f"Step {step+1}: L_ego = {l_ego:.4f}, L_self = {l_self:.4f}")

    print("\nVerification complete.")


if __name__ == "__main__":
    run_verification()
