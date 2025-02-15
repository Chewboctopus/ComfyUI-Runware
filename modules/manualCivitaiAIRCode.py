class manualCivitaiAIRCode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Civitai AIR Code": ("STRING", {
                    "tooltip": "Enter the civitai AIR code manually.",
                }),
                "weight": ("FLOAT", {
                    "tooltip": "Defines the strength or influence of the LoRA model in the generation process.",
                    "default": 1.0,
                    "min": -4.0,
                    "max": 4.0,
                    "step": 0.1,
                }),
            },
        }

    DESCRIPTION = "Manually enter a civitai AIR code and connect it to Runware Inference Nodes in ComfyUI."
    FUNCTION = "manualCivitaiAIRCode"
    RETURN_TYPES = ("RUNWARELORA",)
    RETURN_NAMES = ("Runware Lora",)
    CATEGORY = "Runware"

    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        return True

    def manualCivitaiAIRCode(self, **kwargs):
        airCode = kwargs.get("Civitai AIR Code")
        loraWeight = kwargs.get("weight")
        return ({
            "model": airCode,
            "weight": round(loraWeight, 2),
        },)
