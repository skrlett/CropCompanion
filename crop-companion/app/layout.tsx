'use client';
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { usePathname } from "next/navigation";
import "./globals.css";
import Navbar from "@/components/Navbar";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const hide_navbar = ["/login", "/signup"];
  const pathName = usePathname();

  return (
    <html lang="en">
      <body>
        {hide_navbar.includes(pathName) ? null : <Navbar />}
        {children}
      </body>
    </html>
  );
}
