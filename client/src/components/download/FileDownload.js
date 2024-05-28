/******************************************************************************
 * Filename: FileDownload.js
 * Purpose:  Provides a button component for downloading MIDI files.
 * Author:   Benjamin Goh
 *
 * Description:
 * This React component renders a button that, when clicked, triggers the download of a
 * MIDI file. The component fetches MIDI file data using a unique MIDI ID from a specified
 * API endpoint and uses the `downloadMidi` utility function to facilitate the download.
 *
 * Usage:
 * To use this component, import it into your React component and pass the required `data`
 * prop which should contain the `midi_id` and `title` of the MIDI file to be downloaded.
 *
 * Example:
 * ```jsx
 * import FileDownload from './path/to/FileDownload';
 *
 * const midiData = { midi_id: '123', title: 'ExampleSong' };
 *
 * function App() {
 *   return (
 *     <div>
 *       <FileDownload data={midiData} />
 *     </div>
 *   );
 * }
 * ```
 *
 * Notes:
 * - Ensure that the `REACT_APP_API_URL` environment variable is set in your environment.
 *   This variable should point to the base URL of your API.
 * - The component expects the API to respond with a JSON object that includes a `midi_data`
 *   field containing base64-encoded MIDI data and a `title` field for the filename.
 * - Error handling is included, logging any errors to the console.
 * - The component is designed to be flexible and can be placed in any part of your React application
 *   where file download functionality is required.
 ******************************************************************************/

import downloadMidi from "../../utils/downloadMidi";

const FileDownload = ({ data }) => {
  // Data is expecting to be a JSON and have midi_id field

  const handleClick = () => {
    const apiUrl = process.env.REACT_APP_API_URL;

    fetch(`${apiUrl}/api/v1/midis/${data.midi_id}`)
      .then((response) => response.json())
      .then((data) => {
        const midiData = data.midi_data; // base64 encoded MIDI data
        const filename = data.title + ".mid"; // Generate a file name

        // Call download function
        downloadMidi(midiData, filename);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return <button onClick={handleClick}>download midi</button>;
};

export default FileDownload;
