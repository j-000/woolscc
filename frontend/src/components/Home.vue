<template>
  <div>
    <div class="row ml-3 mr-3">
      <div class="col">
        <input  v-model="url" class="input_1" type="text" placeholder="URL to shorten">
        <button v-if="url" @click="getShortLink" href="javascript:void(0)" class="btn btn-lg btn-success mt-5">Get short link</button>
        <div v-if="link.follow_url" class="bg-light p-2 mt-5">
          <h1 id="url_h1">{{link.follow_url.substring(8)}}</h1>
          <h5 v-if="link" class="mt-4">Original: {{ link.original_url.substring(0, 30) }}</h5>
        </div>
        <button v-if="link"  @click="copyTextToClipboard" class="mb-3 btn btn-lg btn-success mt-5">Copy link</button>
        <div v-else class="p-2 mt-5">
          <h1 id="url_h1">... meh ...</h1>
        </div>
        <p v-if="copied_msg" class="mb-3 bg-success text-white pl-2 pr-2">{{ copied_msg }}</p>
        <p>That's Baaarbara, by the way, and she follows *anything*! If you ask me, I would say she's a sheep...</p>
        <p>Links are valid for <strong>30 days</strong> and then they are turned into woolly jumpers... 🐑.</p>
      </div>
      <div class="col text-center">
        <img src="../static/sheep_1.png" alt="wools ewe">
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
      copied_msg: false
    }
  },
  methods:{
    getShortLink(){
      if(this.url != ''){
        axios.get(`${host}?url=${this.url}`)
        .then((response) => {
          this.url = '';
          this.link = response.data;
        })
        .catch((error) => {console.log(error)});
      }
    },
    copyTextToClipboard() {
      navigator.clipboard.writeText(this.link.follow_url).then(() => {
        this.copied_msg = 'Link copied!';
        setTimeout(() => {
          this.copied_msg = '';
        }, 2000);
      }, function(err) {
        console.error('Async: Could not copy text: ', err);
      });
    }
  }
}
</script>

<style>
img{
  max-width: 80%;
  min-width: 300px;
}
html > body{
  background: rgba(255, 238, 0, 0.6);
}
h1#title{
  font-size: 55pt!important;
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
.btn-lg{
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