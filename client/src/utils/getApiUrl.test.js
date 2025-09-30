/******************************************************************************
 * Filename: getApiUrl.test.js
 * Purpose:  Unit tests for getApiUrl.js utility function.
 * Author:   Darren Seubert
 *
 * Description:
 * This file contains tests for the getApiUrl function, ensuring it returns the
 * correct API URL based on the NODE_ENV environment variable and the relevant
 * REACT_APP_API_URL_* variables.
 *
 * Usage:
 * Run the tests using the command `npm test` or `yarn test`.
 ******************************************************************************/

import { getApiUrl } from "./getApiUrl";

describe("getApiUrl", () => {
  const OLD_ENV = process.env;

  beforeEach(() => {
    jest.resetModules();
    process.env = { ...OLD_ENV };
  });

  afterEach(() => {
    process.env = OLD_ENV;
  });

  it("returns REACT_APP_API_URL_PROD when NODE_ENV is production", () => {
    process.env.NODE_ENV = "production";
    process.env.REACT_APP_API_URL_PROD = "https://prod.example.com";
    process.env.REACT_APP_API_URL_DEV = "https://dev.example.com";
    expect(getApiUrl()).toBe("https://prod.example.com");
  });

  it("returns REACT_APP_API_URL_DEV when NODE_ENV is not production", () => {
    process.env.NODE_ENV = "development";
    process.env.REACT_APP_API_URL_PROD = "https://prod.example.com";
    process.env.REACT_APP_API_URL_DEV = "https://dev.example.com";
    expect(getApiUrl()).toBe("https://dev.example.com");
  });

  it("returns undefined if REACT_APP_API_URL_PROD is missing in production", () => {
    process.env.NODE_ENV = "production";
    delete process.env.REACT_APP_API_URL_PROD;
    process.env.REACT_APP_API_URL_DEV = "https://dev.example.com";
    expect(getApiUrl()).toBeUndefined();
  });

  it("returns undefined if REACT_APP_API_URL_DEV is missing in development", () => {
    process.env.NODE_ENV = "development";
    process.env.REACT_APP_API_URL_PROD = "https://prod.example.com";
    delete process.env.REACT_APP_API_URL_DEV;
    expect(getApiUrl()).toBeUndefined();
  });
});
