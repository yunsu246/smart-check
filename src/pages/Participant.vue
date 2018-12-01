<template>
  <v-ons-page>
    <div class="camera">
      <div class="focus">
        <p class="intro">result: <b>{{ result }}</b></p>
        <qrcode-drop-zone @decode="onDecode" @init="logErrors">
          <qrcode-stream :camera="{ facingMode }" @init="onInit">
            <button @click="switchCamera">Switch Camera</button>
          </qrcode-stream>
        </qrcode-drop-zone>

        <qrcode-capture v-if="noStreamApiSupport" @decode="onDecode" />
      </div>
    </div>
  </v-ons-page>
</template>

<script>
const REAR_CAMERA = { ideal: 'environment' }
const FRONT_CAMERA = { exact: 'user' }

export default {
  data () {
    return {
      result: '',
      facingMode: REAR_CAMERA,
      noFrontCamera: false,
      noStreamApiSupport: false
    }
  },

  methods: {
    onDecode (result) {
      this.result = result
    },

    logErrors (promise) {
      promise.catch(console.error)
    },

    switchCamera () {
      if (this.facingMode === FRONT_CAMERA) {
        this.facingMode = REAR_CAMERA
      } else {
        this.facingMode = FRONT_CAMERA
      }
    },

    async onInit (promise) {
      try {
        await promise
      } catch (error) {
        if (error.name === 'StreamApiNotSupportedError') {
          this.noStreamApiSupport = true
          this.noFrontCamera = this.facingMode === FRONT_CAMERA
            && error.name === 'OverconstrainedError'

          console.error(error)
        }
      }
    }
  }
}
</script>

<style scoped>
button {
  position: absolute;
  left: 10px;
  top: 10px;
}
.camera {
  width: 100%;
  height: 100%;
  background-color: lightgrey;
  vertical-align: middle;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.focus {
  width: 100%;
  height: 100%;
}
</style>



