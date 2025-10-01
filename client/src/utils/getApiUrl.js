/******************************************************************************
 * Filename: getApiUrl.js
 * Purpose:  Returns the correct API base URL depending on the environment 
 * (development or production).
 * Author:   Darren Seubert
 *
 * Description:
 * This module provides a helper function to select the appropriate API base
 * URL for the frontend application, based on whether the app is running in
 * development or production mode. It checks the NODE_ENV environment variable
 * and returns either the development or production API URL as defined in the
 * environment variables.
 *
 * Usage:
 * Import the `getApiUrl` function from this module and call it to get the
 * correct API URL:
 *
 * ```javascript
 * import { getApiUrl } from './getApiUrl';
 *
 * const apiUrl = getApiUrl();
 * fetch(`${apiUrl}/api/v1/midis`);
 * ```
 *
 * Notes:
 * - This function assumes that both REACT_APP_API_URL_DEV and
 *   REACT_APP_API_URL_PROD are defined in your environment at build time.
 * - If either variable is missing, the function will return undefined.
 ******************************************************************************/

export function getApiUrl() {
  return process.env.NODE_ENV === "production"
    ? process.env.REACT_APP_API_URL_PROD
    : process.env.REACT_APP_API_URL_DEV;
}