import requests
import json

# 프록시 서버 URL
BASE_URL = "http://localhost:8000/v1"

def test_chat_completion():
    """Chat Completion API 테스트"""
    url = f"{BASE_URL}/chat/completions"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print("\n=== Chat Completion API 테스트 ===")
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"에러 발생: {str(e)}")

def test_embedding():
    """Embedding API 테스트"""
    url = f"{BASE_URL}/embeddings"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "text-embedding-ada-002",
        "input": "Hello, world!"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print("\n=== Embedding API 테스트 ===")
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"에러 발생: {str(e)}")

if __name__ == "__main__":
    print("API 테스트를 시작합니다...")
    test_chat_completion()
    test_embedding()
