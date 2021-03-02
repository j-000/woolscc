<template>
  <div>
    <div class="row ml-3 mr-3">
      <div class="col">
        <input  v-model="url" class="input_1" type="text" placeholder="URL to shorten">
        <a  @click="getShortLink" href="javascript:void(0)" class="btn btn-lg btn-success mt-5">Get short link</a>
        <div v-if="link.follow_url" class="bg-light p-2 mt-5">
          <h1 @click="copyTextToClipboard" id="url_h1">{{link.follow_url}}</h1>
          <h5 v-if="link" class="mt-4">Original: {{ link.original_url.substring(0, 30) }}</h5>
        </div>
        <div v-else class="p-2 mt-5">
          <h1 id="url_h1">... meh ...</h1>
        </div>
        <div class="row mt-5">
          <div class="col">
            <p>That's Baaarbara, by the way, and she follows *anything*! If you ask me, I would say she's a sheep...</p>
            <p>Links are valid for <strong>30 days</strong> and then they are turned into woolly jumpers... meh.</p>
          </div>
        </div>
      </div>
      <div class="col text-center">
        <h1 id="title">wools.cc</h1>
        <div>
          <img v-if="ewe_image_1" width="500" src="../static/sheep_1.png" alt="wools ewe">
          <img v-else width="600" src="../static/sheep_2.png" alt="wools ewe">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import host from '../main';
import axios from 'axios';


export default {
  name: 'Home',
  data(){
    return {
      url: '',
      link: false,
      ewe_image_1: true
    }
  },
  methods:{
    getShortLink(){
      this.ewe_image_1 = !this.ewe_image_1;
      if(this.url != ''){
        axios.get(`${host}?url=${this.url}`)
        .then((response) => {
          console.log(response);
          this.url = '';
          this.link = response.data;
        })
        .catch((error) => {alert(error)});
      }
    },
    copyTextToClipboard() {
      navigator.clipboard.writeText(this.link.follow_url).then(function() {
        console.log('Async: Copying to clipboard was successful!');
      }, function(err) {
        console.error('Async: Could not copy text: ', err);
      });
    }
  }
}
</script>

<style>
html > body{
  background: rgba(255, 238, 0, 0.6);
}
h1#title{
  font-size: 55pt!important;
}
h1#url_h1{
  cursor: pointer;

}


small{
  font-size: 10pt!important;
}
p{
  font-size: 25pt;
  text-align: justify;
}
.input_1{
  font-size: 30pt!important;
  display: block;
  width: 100%;
  margin: auto;
}
.btn-success{
  background-color: rgba(61, 71, 84, 1)!important;
}

/* #clipboard_icon{
  height: 50px!important;
  width: 50px!important;
}

#clipboard_icon:hover{
  cursor: pointer;
}
*/
</style>