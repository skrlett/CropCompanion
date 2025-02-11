import Link from "next/link";

export default function Navbar() {
    return (
        <header className="bg-gray-800 py-4 text-white shadow-md">
            <nav className="flex justify-between items-center w-[92%] mx-auto">
                <div className="w-16 font-bold text-lime-400">
                    CropCompanion
                </div>
                <div className="nav-links duration-500 md:static 
                            absolute md:min-h-fit min-h-[60vh] 
                            left-0 top-[-100%] md:w-auto w-full 
                            flex items-center px-5">
                    <ul className="flex md:flex-row flex-col 
                            md:items-center md:gap-[4vw] gap-8">
                        <li>
                            <Link className="hover:text-lime-400 transition duration-200" href="/">Home</Link>
                        </li>
                        <li>
                            <Link className="hover:text-lime-400 transition duration-200" href="/chat">Chat Page</Link>
                        </li>
                        <li>
                            <Link className="hover:text-lime-400 transition duration-200" href="/">Contact Support</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </header>
    );
}
