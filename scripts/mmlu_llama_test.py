from main import EvalConfig, run_eval

MODEL = "llama3-8b-pretrain"


def get_llama8b_config(k_shot: int) -> EvalConfig:
    return EvalConfig(
        model_loader="llama",
        model=MODEL,
        eval_name="mmlu",
        num_examples=10,
        k_shots=k_shot,
        output_dir="output",
    )


for k_shot in [0, 1, 2, 3, 4, 5, 10, 20]:
    run_eval(get_llama8b_config(k_shot))
