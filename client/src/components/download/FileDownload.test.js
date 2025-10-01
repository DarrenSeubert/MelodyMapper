/******************************************************************************
 * Filename: FileDownload.test.js
 * Purpose:  Tests the FileDownload component.
 * Author:   Victor Nguyen & Darren Seubert
 *
 * Description:
 * This file contains tests for the FileDownload component. The tests ensure that
 * the component correctly fetches MIDI file data and initiates a download when the
 * download button is clicked. The tests mock the necessary functions to prevent
 * actual fetch requests during testing.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 *
 ******************************************************************************/

import { render, fireEvent, screen, waitFor } from "@testing-library/react";
import FileDownload from "./FileDownload";
import { getApiUrl } from "../../utils/getApiUrl";

jest.mock("../../utils/downloadMidi", () => jest.fn());

describe("FileDownload", () => {
  it("should call downloadMidi function on button click", () => {
    const data = { midi_id: "123", title: "test" };
    const apiUrl = getApiUrl();
    const midiData = "base64 encoded MIDI data";

    global.fetch = jest.fn().mockResolvedValueOnce({
      json: jest.fn().mockResolvedValueOnce({ midi_data: midiData }),
    });

    render(<FileDownload data={data} />);

    fireEvent.click(screen.getByText("download midi"));

    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith(
      `${apiUrl}/api/v1/midis/${data.midi_id}`,
    );
  });

  it("should log error on fetch failure", async () => {
    const data = { midi_id: "123", title: "test" };
    const error = new Error("Fetch failed");

    // Mock fetch to reject with an error
    global.fetch = jest.fn().mockRejectedValueOnce(error);

    // Mock console.error to keep the error from appearing in the test output
    console.error = jest.fn();

    render(<FileDownload data={data} />);

    fireEvent.click(screen.getByText("download midi"));

    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith(
      `${process.env.REACT_APP_API_URL}/api/v1/midis/${data.midi_id}`,
    );

    // Use waitFor to wait for the fetch request to fail and console.error to be called
    await waitFor(() => {
      expect(console.error).toHaveBeenCalledTimes(1);
    });
  });
});
