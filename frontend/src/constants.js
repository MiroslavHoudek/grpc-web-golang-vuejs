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
    console.log('Full screen request succeeded')
  })
  .catch(err => { // v1.5.0+
    console.log('Full screen request error', err)
  })

// Exiting fullscreen mode:
AppFullscreen.exit()
  .then(() => { // v1.5.0+
    console.log('Full screen exit succeeded')
  })
  .catch(err => { // v1.5.0+
    // oh, no!!!
    console.log('Full screen exit error', err)
  })
