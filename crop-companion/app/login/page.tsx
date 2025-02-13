import Link from "next/link";
export default function LoginForm() {
    return (
      <div className="flex flex-col h-screen bg-gray-900 text-white items-center justify-center p-6">
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg w-full max-w-md">
          <h2 className="text-xl font-semibold mb-4 text-center">Login</h2>
          <form className="space-y-4">
            {/* Email Field */}
            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-300">
                Email
              </label>
              <input
                type="email"
                id="email"
                name="email"
                required
                className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            
            {/* Password Field */}
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-300">
                Password
              </label>
              <input
                type="password"
                id="password"
                name="password"
                required
                className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
  
            {/* Submit Button */}
            <button
              type="submit"
              className="w-full p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200"
            >
              Login
            </button>
            
            {/* Forgot Password & Signup Links */}
            <div className="text-sm text-center mt-2">
              <a href="#" className="text-blue-400 hover:underline">
                Forgot password?
              </a>
            </div>
            <div className="text-sm text-center">
              Don't have an account?{" "}
              <Link href="/signup" className="text-blue-400 hover:underline">
                Sign up
              </Link>
            </div>
          </form>
        </div>
      </div>
    );
  }
  