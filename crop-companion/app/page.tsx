export default function SoilDataForm() {
  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white items-center justify-center p-6">
      <div className="bg-gray-800 p-6 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-xl font-semibold mb-4 text-center">Soil Data Form</h2>
        <form className="space-y-4">
          <div>
            <label htmlFor="Location" className="block text-sm font-medium text-gray-300">
              Please enter your location
            </label>
            <input
              type="text"
              id="Location"
              name="Location"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label htmlFor="SoilType" className="block text-sm font-medium text-gray-300">
              Please enter your soil type
            </label>
            <input
              type="text"
              id="SoilType"
              name="SoilType"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <button
            type="submit"
            className="w-full p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}
