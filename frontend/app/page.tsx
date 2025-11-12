import BrailleConverter from '@/app/components/BrailleConverter';

export default function Home() {
  return (
    <main className="min-h-screen p-8 bg-gradient-to-br from-gray-50 to-blue-50">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            점자닷
          </h1>
          <p className="text-xl text-gray-600 mb-2">
            한글 점자 변환기
          </p>
          <p className="text-sm text-gray-500">
            한글 텍스트를 점자로 쉽고 빠르게 변환하세요
          </p>
        </div>

        <BrailleConverter />

        <footer className="mt-16 text-center text-sm text-gray-500">
          <p>
            점자닷 v0.1.0 | Rule-based 한글 점자 변환
          </p>
          <p className="mt-2">
            문의 사항이 있으시면 이슈를 등록해주세요
          </p>
        </footer>
      </div>
    </main>
  );
}
