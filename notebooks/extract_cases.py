from phi.agent import Agent
from phi.model.ollama import Ollama

extract_agent = Agent(
    model=Ollama(id="iodose/nuextract-v1.5"),
    description="You extract information.",
)

def predict_nuextract(input_text):
    template = """
    {
        "Customer": {
            "Name": "",
            "Address": "",
            "Policy Number": "",
            "Telephone Number": "",
        },
        "Case": {
            "Accident Location": ""
            "Time": ""
        }
    }
    """
    template = f"""<|input|>\n ###Template:\n{template}\n### Text:\n{input_text}\n\n<|output|>"""

    return template

case1 = """
Dear Parasol Insurance,\n\nI hope this email finds you well. My name is Sarah Turner, and I am writing to file a claim for a recent car accident that occurred on January 2nd, 2024, at approximately 3:30 PM. My policy number is AC-987654321.\n\nThe accident took place at the intersection of Birch Street and Willow Avenue in the city of Evergreen. I was driving my vehicle, a black Toyota Camry with license plate number DEF-456, heading south on Birch Street. At the intersection, the traffic signal was green, and I proceeded through the intersection.\n\nAt the same time, another vehicle, a blue Chevrolet Traverse with license plate number GHI-789, was traveling west on Willow Avenue. Unfortunately, the driver failed to stop at the red traffic signal, resulting in a collision with the front passenger side of my vehicle.\n\nThe impact caused significant damage to both vehicles. The front bumper and right headlight of my Toyota Camry are extensively damaged, and there are also damages to the front driver's side of the Chevrolet Traverse. Fortunately, no injuries were sustained during the accident, and both drivers were able to move their vehicles to the side of the road.\n\nI promptly exchanged information with the other driver, Mr. Daniel Reynolds, including our names, phone numbers, insurance details, and a brief description of the accident. Additionally, I took photos of the accident scene, including the damages to both vehicles and the position of the traffic signal.\n\nI have attached the necessary documents to this email, including the photos, a copy of the police report filed at the Evergreen Police Department, and the estimate for the repair costs from Evergreen Auto Repair, where I have taken my vehicle for assessment.\n\nI kindly request your prompt attention to this matter and would appreciate any guidance on the next steps in the claims process. If you require any additional information or documentation, please do not hesitate to contact me at (555) 123-4567 or sarah.turner@email.com.\n\nThank you for your assistance, and I look forward to a swift resolution of this claim.\n\nSincerely,\n\nSarah Turner\n123 Oak Street\nEvergreen, CA 98765\n(555) 123-4567\nsarah.turner@email.com
    """

print(predict_nuextract(case1))

extract_agent.print_response(predict_nuextract(case1))