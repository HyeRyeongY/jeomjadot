/**
 * Backend API 클라이언트
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface TranslateRequest {
  text: string;
  use_liblouis?: boolean;
}

export interface TranslateResponse {
  original_text: string;
  braille: string;
  method: string;
  success: boolean;
  error?: string | null;
}

/**
 * 텍스트를 점자로 변환
 */
export async function translateToBraille(
  request: TranslateRequest
): Promise<TranslateResponse> {
  const response = await fetch(`${API_URL}/api/translate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || '점자 변환에 실패했습니다');
  }

  return response.json();
}

/**
 * API 상태 확인
 */
export async function checkHealth(): Promise<{ status: string; liblouis_available: boolean }> {
  const response = await fetch(`${API_URL}/api/translate/health`);

  if (!response.ok) {
    throw new Error('API 상태 확인에 실패했습니다');
  }

  return response.json();
}
