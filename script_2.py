
import json
def main(params):
    # Effectuez vos opérations dans action2 en utilisant la valeur passée
    initialValue = params.get('initialValue', 0)
    result = initialValue * 2

    if isinstance(result, (int, float)):
        return {"msg": "Hi, your inital value is doubled: " + str(result),
                "initialValue":initialValue,
                "secondValue": result}
    else:
        return {"error": "Invalid result type"}