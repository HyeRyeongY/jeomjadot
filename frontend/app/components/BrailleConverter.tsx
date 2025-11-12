'use client';

import { useState, useEffect } from 'react';
import { translateToBraille, checkHealth, type TranslateResponse } from '@/app/lib/api';
import BrailleRulesModal from './BrailleRulesModal';

export default function BrailleConverter() {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState<TranslateResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [apiStatus, setApiStatus] = useState<'checking' | 'online' | 'offline'>('checking');
  const [liblouisAvailable, setLiblouisAvailable] = useState(false);
  const [useLiblouis, setUseLiblouis] = useState(false);
  const [showRulesModal, setShowRulesModal] = useState(false);

  // API 상태 확인
  useEffect(() => {
    checkHealth()
      .then((status) => {
        setApiStatus('online');
        setLiblouisAvailable(status.liblouis_available);
      })
      .catch(() => {
        setApiStatus('offline');
      });
  }, []);

  const handleConvert = async () => {
    if (!inputText.trim()) {
      setError('텍스트를 입력해주세요');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await translateToBraille({
        text: inputText,
        use_liblouis: useLiblouis,
      });

      if (response.success) {
        setResult(response);
      } else {
        setError(response.error || '변환에 실패했습니다');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : '알 수 없는 오류가 발생했습니다');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && e.ctrlKey) {
      handleConvert();
    }
  };

  const copyToClipboard = async () => {
    if (result?.braille) {
      try {
        await navigator.clipboard.writeText(result.braille);
        alert('점자 텍스트가 클립보드에 복사되었습니다!');
      } catch (err) {
        alert('클립보드 복사에 실패했습니다');
      }
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      {/* API 상태 표시 */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2">
            <div
              className={`w-3 h-3 rounded-full ${
                apiStatus === 'online'
                  ? 'bg-green-500'
                  : apiStatus === 'offline'
                  ? 'bg-red-500'
                  : 'bg-yellow-500 animate-pulse'
              }`}
            />
            <span className="text-sm text-gray-600">
              {apiStatus === 'online'
                ? 'API 연결됨'
                : apiStatus === 'offline'
                ? 'API 연결 실패 (백엔드를 실행해주세요)'
                : 'API 확인 중...'}
            </span>
          </div>

          <button
            onClick={() => setShowRulesModal(true)}
            className="flex items-center gap-1 px-3 py-1 text-sm text-blue-600 hover:text-blue-800 border border-blue-600 rounded-lg hover:bg-blue-50 transition-colors"
          >
            <svg
              className="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            점자 규칙 보기
          </button>
        </div>

        {liblouisAvailable && (
          <label className="flex items-center gap-2 text-sm cursor-pointer">
            <input
              type="checkbox"
              checked={useLiblouis}
              onChange={(e) => setUseLiblouis(e.target.checked)}
              className="w-4 h-4"
            />
            <span>libLouis 사용</span>
          </label>
        )}
      </div>

      {/* 입력 영역 */}
      <div className="space-y-2">
        <label htmlFor="input-text" className="block text-lg font-semibold text-gray-700">
          한글 텍스트 입력
        </label>
        <textarea
          id="input-text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="점자로 변환할 한글 텍스트를 입력하세요...&#10;&#10;예: 안녕하세요"
          className="w-full h-40 p-4 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none resize-none text-lg"
          disabled={apiStatus === 'offline'}
        />
        <p className="text-sm text-gray-500">
          Ctrl + Enter로 빠르게 변환할 수 있습니다
        </p>
      </div>

      {/* 변환 버튼 */}
      <button
        onClick={handleConvert}
        disabled={loading || apiStatus === 'offline'}
        className="w-full py-3 px-6 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
      >
        {loading ? '변환 중...' : '점자로 변환'}
      </button>

      {/* 오류 메시지 */}
      {error && (
        <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
          <p className="text-red-700">{error}</p>
        </div>
      )}

      {/* 결과 영역 */}
      {result && (
        <div className="space-y-4 p-6 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-lg border-2 border-blue-200">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-bold text-gray-800">점자 변환 결과</h2>
            <div className="flex items-center gap-4">
              <span className="text-sm text-gray-600">
                변환 방법: <span className="font-semibold">{result.method}</span>
              </span>
              <button
                onClick={copyToClipboard}
                className="px-3 py-1 text-sm bg-white border border-gray-300 rounded hover:bg-gray-50 transition-colors"
              >
                복사
              </button>
            </div>
          </div>

          <div className="p-4 bg-white rounded-lg border border-gray-200">
            <p className="text-3xl leading-relaxed break-words" style={{ fontFamily: 'monospace' }}>
              {result.braille}
            </p>
          </div>

          <div className="text-sm text-gray-600">
            <p>원본: {result.original_text}</p>
          </div>
        </div>
      )}

      {/* 점자 규칙 모달 */}
      <BrailleRulesModal
        isOpen={showRulesModal}
        onClose={() => setShowRulesModal(false)}
      />
    </div>
  );
}
