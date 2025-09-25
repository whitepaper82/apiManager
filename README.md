# OpenAI API 프록시 서버

이 프로젝트는 OpenAI API를 중계하는 프록시 서버입니다. 여러 클라이언트가 하나의 OpenAI API 키를 안전하게 공유할 수 있도록 해줍니다.

## 설치 방법

1. 저장소를 클론합니다:
```bash
git clone [repository-url]
cd [repository-name]
```

2. 가상 환경을 생성하고 활성화합니다:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. 필요한 패키지를 설치합니다:
```bash
pip install -r requirements.txt
```

4. 환경 변수를 설정합니다:
   - `.env.example` 파일을 `.env`로 복사합니다
   - `.env` 파일에 OpenAI API 키를 입력합니다

## 실행 방법

서버를 시작하려면 다음 명령어를 실행합니다:

```bash
python main.py
```

또는:

```bash
uvicorn main:app --reload
```

서버는 기본적으로 `http://localhost:8000`에서 실행됩니다.

## API 엔드포인트

현재 지원되는 엔드포인트:

- POST `/v1/chat/completions` - ChatGPT API
- POST `/v1/embeddings` - 임베딩 API

각 엔드포인트는 OpenAI API와 동일한 요청 형식을 사용합니다.

## 보안 고려사항

실제 운영 환경에서는 다음 사항을 고려하세요:

- CORS 설정을 구체적인 origin으로 제한
- API 키 인증 추가
- 요청 속도 제한 설정
- HTTPS 사용
