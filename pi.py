import random

DEFAULT_ITERATIONS = 10000


def predict(req):
    """Wrapper for estimate_pi that turns it into a CML model.

    The incoming request is a Python dictionary. If present, the value of the key "n_iterations" is passed to estimate_pi.
    """
    n_iterations = req.get("n_iterations", DEFAULT_ITERATIONS)
    return estimate_pi(n_iterations)


def estimate_pi(n_iterations):
    """Returns an estimate of pi computed using Monte-Carlo integration."""
    successes = 0
    for _ in range(n_iterations):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x ** 2 + y ** 2 < 1:
            successes += 1
    return 4.0 * successes / n_iterations
