export default function SoilDataForm() {
  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white items-center justify-center p-6">
      <div className="bg-gray-800 p-6 rounded-lg shadow-lg w-full max-w-xl">
        <h2 className="text-xl font-semibold mb-4 text-center">Soil Data Form</h2>
        <form className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="col-span-2">
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
              Soil Type
            </label>
            <input
              type="text"
              id="SoilType"
              name="SoilType"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label htmlFor="SoilPh" className="block text-sm font-medium text-gray-300">
              Soil pH
            </label>
            <input
              type="text"
              id="SoilPh"
              name="SoilPh"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <fieldset className="col-span-2 border border-gray-600 p-4 rounded-lg">
            <legend className="text-sm font-medium text-gray-300 px-2">Nutrient Content</legend>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label htmlFor="Nitrogen" className="block text-sm font-medium text-gray-300">
                  Nitrogen Content
                </label>
                <input
                  type="text"
                  id="Nitrogen"
                  name="Nitrogen"
                  required
                  className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label htmlFor="Phosphorous" className="block text-sm font-medium text-gray-300">
                  Phosphorous Content
                </label>
                <input
                  type="text"
                  id="Phosphorous"
                  name="Phosphorous"
                  required
                  className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label htmlFor="Potassium" className="block text-sm font-medium text-gray-300">
                  Potassium Content
                </label>
                <input
                  type="text"
                  id="Potassium"
                  name="Potassium"
                  required
                  className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>
          </fieldset>

          <div>
            <label htmlFor="Temperature" className="block text-sm font-medium text-gray-300">
              Temperature
            </label>
            <input
              type="text"
              id="Temperature"
              name="Temperature"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label htmlFor="Rainfall" className="block text-sm font-medium text-gray-300">
              Rainfall
            </label>
            <input
              type="text"
              id="Rainfall"
              name="Rainfall"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="col-span-2">
            <label htmlFor="Humidity" className="block text-sm font-medium text-gray-300">
              Humidity Content
            </label>
            <input
              type="text"
              id="Humidity"
              name="Humidity"
              required
              className="w-full p-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <button
            type="submit"
            className="col-span-2 p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}
