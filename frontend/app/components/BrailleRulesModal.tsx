'use client';

import { useState, useEffect } from 'react';

interface BrailleExample {
  korean: string;
  braille: string;
  description: string;
}

interface BrailleRule {
  title: string;
  note?: string;
  examples: BrailleExample[];
}

interface BrailleCategory {
  id: string;
  title: string;
  description: string;
  rules: BrailleRule[];
}

interface BrailleRulesData {
  title: string;
  source: string;
  reference_url: string;
  categories: BrailleCategory[];
  notes: string[];
}

interface BrailleRulesModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function BrailleRulesModal({ isOpen, onClose }: BrailleRulesModalProps) {
  const [rulesData, setRulesData] = useState<BrailleRulesData | null>(null);
  const [activeTab, setActiveTab] = useState('basic');

  useEffect(() => {
    // 규칙 데이터 로드
    fetch('/braille_rules_reference.json')
      .then((res) => res.json())
      .then((data) => setRulesData(data))
      .catch((err) => console.error('규칙 데이터 로드 실패:', err));
  }, []);

  if (!isOpen || !rulesData) return null;

  const activeCategory = rulesData.categories.find((cat) => cat.id === activeTab);

  return (
    <div className="fixed inset-0 z-50 overflow-hidden">
      {/* 배경 오버레이 */}
      <div
        className="absolute inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={onClose}
      />

      {/* 모달 컨테이너 */}
      <div className="absolute inset-y-0 right-0 max-w-4xl w-full bg-white shadow-xl flex flex-col">
        {/* 헤더 */}
        <div className="px-6 py-4 border-b border-gray-200 flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">{rulesData.title}</h2>
            <p className="text-sm text-gray-600 mt-1">
              {rulesData.source}
            </p>
            <a
              href={rulesData.reference_url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-blue-600 hover:text-blue-800 underline mt-1 inline-block"
            >
              국립국어원 원문 보기 →
            </a>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 text-3xl leading-none"
          >
            ×
          </button>
        </div>

        {/* 탭 메뉴 */}
        <div className="px-6 py-3 border-b border-gray-200 overflow-x-auto">
          <div className="flex space-x-2">
            {rulesData.categories.map((category) => (
              <button
                key={category.id}
                onClick={() => setActiveTab(category.id)}
                className={`px-4 py-2 rounded-lg font-medium whitespace-nowrap transition-colors ${
                  activeTab === category.id
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                {category.title}
              </button>
            ))}
          </div>
        </div>

        {/* 내용 영역 */}
        <div className="flex-1 overflow-y-auto px-6 py-6">
          {activeCategory && (
            <div>
              <p className="text-gray-700 mb-6">{activeCategory.description}</p>

              {activeCategory.rules.map((rule, ruleIndex) => (
                <div key={ruleIndex} className="mb-8">
                  <h3 className="text-lg font-semibold text-gray-800 mb-3">
                    {rule.title}
                  </h3>
                  {rule.note && (
                    <p className="text-sm text-gray-600 mb-3 italic">
                      {rule.note}
                    </p>
                  )}

                  <div className="space-y-2">
                    {rule.examples.map((example, exIndex) => (
                      <div
                        key={exIndex}
                        className="flex items-center p-3 bg-gray-50 rounded-lg border border-gray-200"
                      >
                        <div className="flex-1 grid grid-cols-3 gap-4">
                          <div>
                            <div className="text-xs text-gray-500 mb-1">원본</div>
                            <div className="font-medium text-gray-900">
                              {example.korean}
                            </div>
                          </div>
                          <div>
                            <div className="text-xs text-gray-500 mb-1">점자</div>
                            <div className="font-mono text-2xl text-blue-600">
                              {example.braille}
                            </div>
                          </div>
                          <div>
                            <div className="text-xs text-gray-500 mb-1">설명</div>
                            <div className="text-sm text-gray-700">
                              {example.description}
                            </div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* 푸터 */}
        <div className="px-6 py-4 border-t border-gray-200 bg-gray-50">
          <div className="text-sm text-gray-600 space-y-1">
            {rulesData.notes.map((note, index) => (
              <p key={index}>• {note}</p>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
