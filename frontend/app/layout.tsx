import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "점자닷 - 한글 점자 변환기",
  description: "한글 텍스트를 점자로 변환하는 웹 애플리케이션",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
