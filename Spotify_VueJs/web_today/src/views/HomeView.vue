<template>
    <div class="flex flex-col text-white h-full w-full gap-5">
        <div class="flex flex-col  w-full gap-3">
            <div class="flex gap-1 text-bold  items-center"><h1>Xin chào</h1><h1 class="text-sky-600 ">ThaiPt</h1><h1>, nghe nhạc</h1></div>
            <div class="flex fill-gray-300 justify-between h-full w-full">
                <svg role="img" height="16" width="16" aria-hidden="true" class="Svg-sc-ytk21e-0 kcBZLg IYDlXmBmmUKHveMzIPCF" viewBox="0 0 16 16" data-encore-id="icon"><path d="M11.03.47a.75.75 0 0 1 0 1.06L4.56 8l6.47 6.47a.75.75 0 1 1-1.06 1.06L2.44 8 9.97.47a.75.75 0 0 1 1.06 0z"></path></svg>
                <h1>{{ counter.show_Ten_nhac }}</h1>
                <svg role="img" height="16" width="16" aria-hidden="true" class="Svg-sc-ytk21e-0 kcBZLg IYDlXmBmmUKHveMzIPCF" viewBox="0 0 16 16" data-encore-id="icon"><path d="M4.97.47a.75.75 0 0 0 0 1.06L11.44 8l-6.47 6.47a.75.75 0 1 0 1.06 1.06L13.56 8 6.03.47a.75.75 0 0 0-1.06 0z"></path></svg>
            </div>
        </div>
        <div class="flex h-[500px] grow gap-5">
            <div class="flex flex-col">
                <div id="cjss" class="w-2/3 flex flex-col overflow-auto">
                    <h1 class="text-[18px]">Bài hát dựa trên tâm trạng của bạn</h1>
                    <div class="flex items-center gap-2">
                        <h1 class="text-[16px]">Danh sách bài hát</h1>
                        <h1 class="text-blue-600 text-[18px] font-bold">{{ counter.Data_Feeling['Data'] }}</h1>
                    </div>
                    <div class="text-white h-full w-full flex flex-col ">
                        <div  class="grid grid-cols-3 border-b-[1px] border-zinc-600 py-5 items-center font-bold">
                            <h1 class="flex w-[250px] ml-[50px]"></h1>
                            <h1 class="flex w-[250px] ml-[50px]">Tên bài hát</h1>
                            <h1>Nghệ sĩ</h1>
                        </div>
                        <div v-for="(i,index) in counter.Data_Feeling['List_Song']" v-on:click=" Play_all(); Get_data_song(i);" class="grid grid-cols-3 text-gray-300 border-b-[1px] border-zinc-600  items-center font-normal py-1 cursor-pointer">
                            <div class="flex gap-5 items-center"><h1>{{ index+1 }}</h1><img :src="counter.domain_Backend+i.poster" class="w-[50px] h-[50px] rounded" /></div>
                            <h1 class="flex w-[250px] ml-[50px]">{{ i.name }}</h1>
                            <h1>{{ i.artist }}</h1>
                        </div>
                    </div>
                </div>
                <h1 class="text-gray-400 text-[20px] font-bold my-5">Danh sách bài hát đã nghe gần đây</h1>
                <div class="flex flex-col">
                    <div v-for="(i,index) in counter.Get_late_song" class="flex text-gray-100 border-b-[1px] border-gray-800 py-3 items-center">
                        <h1 class="w-[15%]">{{ index+1 }}</h1>
                        <div v-on:click=" Play_all(); Get_data_song_1(i); " class="flex w-[35%] gap-3 cursor-pointer">
                            <img :src="i.poster" class="w-[50px] h-[50px] rounded"/>
                            <div class="flex flex-col gap-2 h-[50px]">
                                <h1 class="text-[16px]">{{ i.name }}</h1>
                                <h1 class="text-[13px] text-gray-400">{{ i.artist }}</h1>
                            </div>
                        </div>
                        <h1 class="w-[20%]"></h1>
                        <div class="w-[10%] cursor-pointer">
                            <svg v-show="i.love=='love'" v-on:click="counter.add_song_love(i.name,i.artist,i.duration,i.poster,i.mp3_file,i.id,counter.Data_User.username); i.love=1; " role="img" height="16" width="16" aria-hidden="true" viewBox="0 0 16 16" data-encore-id="icon" class="Svg-sc-ytk21e-0 gQUQL fill-gray-200"><path d="M1.69 2A4.582 4.582 0 0 1 8 2.023 4.583 4.583 0 0 1 11.88.817h.002a4.618 4.618 0 0 1 3.782 3.65v.003a4.543 4.543 0 0 1-1.011 3.84L9.35 14.629a1.765 1.765 0 0 1-2.093.464 1.762 1.762 0 0 1-.605-.463L1.348 8.309A4.582 4.582 0 0 1 1.689 2zm3.158.252A3.082 3.082 0 0 0 2.49 7.337l.005.005L7.8 13.664a.264.264 0 0 0 .311.069.262.262 0 0 0 .09-.069l5.312-6.33a3.043 3.043 0 0 0 .68-2.573 3.118 3.118 0 0 0-2.551-2.463 3.079 3.079 0 0 0-2.612.816l-.007.007a1.501 1.501 0 0 1-2.045 0l-.009-.008a3.082 3.082 0 0 0-2.121-.861z"></path></svg>
                            <svg v-show="i.love==1" v-on:click="counter.delete_song_love(i.name)" role="img" height="16" width="16" aria-hidden="true" viewBox="0 0 16 16" data-encore-id="icon" class="Svg-sc-ytk21e-0 gQUQL absolute fill-green-500"><path d="M15.724 4.22A4.313 4.313 0 0 0 12.192.814a4.269 4.269 0 0 0-3.622 1.13.837.837 0 0 1-1.14 0 4.272 4.272 0 0 0-6.21 5.855l5.916 7.05a1.128 1.128 0 0 0 1.727 0l5.916-7.05a4.228 4.228 0 0 0 .945-3.577z"></path></svg>
                        </div>
                        <h1 class="w-[10%]">{{ i.duration }}</h1>
                        <!-- <div class="w-[10%] cursor-pointer relative">
                            <font-awesome-icon icon="fa-solid fa-ellipsis" />
                        </div> -->
                    </div>
                </div>
            </div>
            <div class="w-1/3 flex flex-col items-center  gap-5  h-full grow shrink-0 mt-[80px]">
                <div class="flex relative">
                    <video id="video" width="320" height="240" autoplay class="bg-red-600 absolute"></video>
                    <canvas id="canvas" width="320" height="240" class=""></canvas>
                </div>
                <button id="snap" v-on:click="Capture(); counter.F_Search_Feeling(); " class="bg-zinc-600 py-2 rounded w-[150px]">Scan</button>
                <!-- <a href="https://www.youtube.com/" target="blank_" class="flex justify-center items-center cursor-pointer bg-zinc-600 py-2 rounded w-[150px]">Chat Bot</a> -->
            </div>
        </div>
    </div>
</template>
<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'
import {PhotoCapture, VideoCapture} from 'vue-media-recorder'



export default {

    data(){
        return {
            canvas: null,
            context: null,
            video:null,
        }
    },
  
  methods: {
    },
    setup() {

        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        this.Play_Video();
        this.counter.get_song_play_list();
        this.counter.get_late_song();
    },
    methods:{
        async Play_all(){
            await this.counter.Play();
            
            this.counter.duration_mp3 = document.getElementById("nhac").onloadedmetadata = ()=> {
            this.counter.duration_mp3 = document.getElementById("nhac").duration;
            this.counter.duration_mp3 = Math.floor(this.counter.duration_mp3);
            if(this.counter.duration_mp3%60 >= 10){
                this.counter.length = Math.floor(this.counter.duration_mp3/60) + ':' + (this.counter.duration_mp3%60)
            }
            else{
                this.counter.length = Math.floor(this.counter.duration_mp3/60) + ':0' + (this.counter.duration_mp3%60)
            } 
            }
        },
        Get_data_song(i){
            this.counter.Play_nhac.URL = this.counter.domain_Backend + i.mp3_file;
            this.counter.Play_nhac.Name_song = i.name;
            this.counter.Play_nhac.Name_artist = i.artist;
            this.counter.Play_nhac.Photo = this.counter.domain_Backend+i.poster;
            this.counter.Pause_Start=true;
        },
        Get_data_song_1(i){
            this.counter.Play_nhac.URL = i.mp3_file;
            this.counter.Play_nhac.Name_song = i.name;
            this.counter.Play_nhac.Name_artist = i.artist;
            this.counter.Play_nhac.Photo = i.poster;
            this.counter.Pause_Start=true;
        }
       ,
        Play_Video(){
            var video = document.getElementById('video');

            // Get access to the camera!
            if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                // Not adding `{ audio: true }` since we only want video now
                navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
                    //video.src = window.URL.createObjectURL(stream);
                    video.srcObject = stream;
                    video.play();
                });
            }
        },
        Capture(){
            this.canvas = document.getElementById('canvas');
            this.context = canvas.getContext('2d');
            this.video = document.getElementById('video');

            // Trigger photo take
             
            this.context.drawImage(this.video, 0, 0, 320, 240);
            this.counter.Image_Base64 = this.canvas.toDataURL();
            this.counter.Image_Base64 = this.counter.Image_Base64.split('data:image/png;base64,')[1];
            
        },
        async Filter_Feeling(){
            await Capture();
            this.counter.F_Search_Feeling();
        }

    }
    ,
    components:{
        PhotoCapture,
        VideoCapture
    }
}
</script>

<style>
#cjss::-webkit-scrollbar {
  width: 10px;               /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #393636;        /* Màu nền ngoài của thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #595857;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
    background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}
</style>


