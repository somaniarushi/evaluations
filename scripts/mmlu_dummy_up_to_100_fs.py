from main import EvalConfig, run_eval


def get_gpt4o_config(k_shot: int) -> EvalConfig:
    return EvalConfig(
        model_loader="openai",
        # model="gpt-4o",
        model="gpt-3.5-turbo",
        eval_name="mmlu",
        num_examples=10,
        k_shots=k_shot,
        output_dir="output",
    )


def get_sonnet_config(k_shot: int) -> EvalConfig:
    return EvalConfig(
        model_loader="anthropic",
        model="claude-3-sonnet",
        eval_name="mmlu",
        num_examples=10,
        k_shots=k_shot,
        output_dir="output",
    )


def get_llama8b_config(k_shot: int) -> EvalConfig:
    return EvalConfig(
        model_loader="llama",
        model="llama3-8b",
        eval_name="mmlu",
        num_examples=10,
        k_shots=k_shot,
        output_dir="output",
    )


for k_shot in [0, 1, 2, 3, 4, 5, 10, 20]:
    run_eval(get_llama8b_config(k_shot))
