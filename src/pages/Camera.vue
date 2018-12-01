<template>
  <v-ons-page>
    <div class="camera">
      <div class="focus">
        <p class="decode-result">Last result: <b>{{ result }}</b></p>

        <qrcode-drop-zone @decode="onDecode" @init="logErrors">
          <qrcode-stream @decode="onDecode" @init="onInit" />
        </qrcode-drop-zone>

        <qrcode-capture v-if="noStreamApiSupport" @decode="onDecode" />
      </div>
    </div>
  </v-ons-page>
</template>

<script>
export default {
  data () {
    return {
      result: '',
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

    async onInit (promise) {
      try {
        await promise
      } catch (error) {
        if (error.name === 'StreamApiNotSupportedError') {
          this.noStreamApiSupport = true
        }
      }
    }
  }
}
</script>

<style scoped>
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
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  border: 12px solid whitesmoke;
}
</style>



