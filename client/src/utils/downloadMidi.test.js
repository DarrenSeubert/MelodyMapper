/******************************************************************************
 * Filename: downloadMidi.test.js
 * Purpose:  Tests the downloadMidi utility function.
 * Author:   Victor Nguyen
 *
 * Description:
 * This file contains tests for the downloadMidi utility function. The tests ensure
 * that the function correctly converts a base64 string to a Blob and initiates a
 * download of the Blob as a file in the browser. The tests mock the necessary
 * functions to prevent actual file downloads during testing.
 *
 * Usage:
 * Run the tests using the command `npm test`.
 *
 ******************************************************************************/

import { JSDOM } from "jsdom";
import { base64ToBlob } from "./downloadMidi";
import downloadMidi from "./downloadMidi";

describe("base64ToBlob", () => {
  // Create a new JSDOM instance before each test
  beforeEach(() => {
    const { window } = new JSDOM();
    global.window = window;
    global.document = window.document;
    global.URL = window.URL;
  });

  // Clean up after each test
  afterEach(() => {
    global.window = undefined;
    global.document = undefined;
    global.URL = undefined;
  });

  it("should convert a base64 string to a Blob", () => {
    const base64String = "SGVsbG8gd29ybGQ="; // 'Hello world' in base64
    const mimeType = "text/plain";

    const result = base64ToBlob(base64String, mimeType);

    expect(result).toBeInstanceOf(Blob);
    expect(result.type).toBe(mimeType);
  });
});

describe("downloadMidi", () => {
  let createElementSpy;
  let appendChildSpy;
  let removeChildSpy;
  let clickSpy;

  beforeEach(() => {
    // Create a new JSDOM instance before each test
    const { window } = new JSDOM();
    global.window = window;
    global.document = window.document;
    global.URL = window.URL;

    // Mock the necessary functions
    global.URL.createObjectURL = jest.fn(() => "blob:mocked");
    createElementSpy = jest
      .spyOn(document, "createElement")
      .mockImplementation(() => ({
        click: (clickSpy = jest.fn()),
      }));
    appendChildSpy = jest
      .spyOn(document.body, "appendChild")
      .mockImplementation(() => {});
    removeChildSpy = jest
      .spyOn(document.body, "removeChild")
      .mockImplementation(() => {});
  });

  afterEach(() => {
    // Clean up the mocks after each test
    createElementSpy.mockRestore();
    appendChildSpy.mockRestore();
    removeChildSpy.mockRestore();
    global.URL.createObjectURL.mockRestore();

    global.window = undefined;
    global.document = undefined;
    global.URL = undefined;
  });

  it("creates a blob and initiates a download", () => {
    // Use a valid base64 string
    const dataBase64 = "SGVsbG8sIHdvcmxkIQ=="; // "Hello, world!" in base64
    const filename = "test.mid";

    downloadMidi(dataBase64, filename);

    // Check that the functions were called with the correct arguments
    expect(global.URL.createObjectURL).toHaveBeenCalled();
    expect(createElementSpy).toHaveBeenCalledWith("a");
    expect(appendChildSpy).toHaveBeenCalled();
    expect(clickSpy).toHaveBeenCalled();
    expect(removeChildSpy).toHaveBeenCalled();
  });
});
