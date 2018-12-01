<template>
  <v-ons-page>
    <p class="intro">
      Input Class Name &amp; Email address to create NEW CLASS.<br><br>
    </p>

    <v-ons-card>
      <div class="card__item">
        <div class="card__title">
          Class Name
        </div>
        <label class="center">
          <v-ons-input float maxlength="30"
            placeholder="Input Class Name"
            v-model="name"
          >
          </v-ons-input>
        </label>
      </div>
      <div class="card__item">
        <div class="card__title">
          Organizer's Email
        </div>
        <label class="center">
          <v-ons-input float maxlength="30"
            placeholder="Input your Email address"
            v-model="name"
          >
          </v-ons-input>
        </label>
      </div>
      <p style="text-align: center">
        <v-ons-button>SUBMIT</v-ons-button>
      </p>
    </v-ons-card>
  </v-ons-page>
</template>

<script>
export default {
  data () {
    return {
      name: ''
    };
  },
}
</script>

<style>
.intro {
  text-align: left;
  padding: 0 22px;
  margin-top: 20px;
  font-size: 14px;
  line-height: 1.4;
  color: rgba(0, 0, 0, .54);
}

ons-card {
  width: 96%;
  height: 60%;
  cursor: pointer;
  color: #333;
}

.card__item {
  padding: 0 22px;
  margin-bottom: 25px;
}

.card__title, .card--material__title {
  font-size: 14px;
}
</style>
