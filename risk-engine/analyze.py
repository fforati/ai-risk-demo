from openai import OpenAI

client = OpenAI()

prompt = """
Analyze this Kubernetes upgrade risk.

Current version:
1.29

Target version:
1.30

Detected deprecated APIs:
- networking.k8s.io/v1beta1 Ingress

Generate:
- risk score 1-10
- compatibility concerns
- recommended tests
"""

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
