export const events = {
  LOADING_START: 'loading_start',
  LOADING_STOP: 'loading_stop',
  DIALOG_ERROR: 'dialog_error_visible',

  SHOW_TERMINAL_DIALOG: 'terminal',
  SHOW_SCREENSHOT_DIALOG: 'screenshot'
}

export const TOKEN_KEY = 'X-CSRF-Token'

export default {
  events,
  TOKEN_KEY
}

import { AppFullscreen } from 'quasar'

// Requesting fullscreen mode:
AppFullscreen.request()
  .then(() => { // v1.5.0+
    // success!
  })
  .catch(err => { // v1.5.0+
    console.log('Inside error, fetching product line items failed', err)
    // oh, no!!!
  })

// Exiting fullscreen mode:
AppFullscreen.exit()
  .then(() => { // v1.5.0+
    // success!
  })
  .catch(err => { // v1.5.0+
    // oh, no!!!
    console.log('Inside error, fetching product line items failed', err)
  })
