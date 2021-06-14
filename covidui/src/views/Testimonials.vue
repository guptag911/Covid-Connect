<template>
  <div>
        <div class="box">
        <div class="corousel">
            <div class="columns">
                <div class="column userImg">
                    <img src="https://www.afro.who.int/sites/default/files/2021-02/COVID-19%20survivor%20supporting%20sensitization%20activities%20in%20Lagos%20i.jpg">
                </div>
                <div class="column">
                    <p>{{ currentU.name }}</p>
                    <p>{{ currentT.exp }}</p>
                    <p> {{ currentT.suggest }}</p>
                </div>
            </div>
        </div>
        </div>
        <footer class="footer">
            <p>Have you also recovered from Covid-19 ? </p>
            <button v-if="!show" class="button is-link" @click="newTestimonial()">Write your experience!</button>
        </footer>
        <div class="modal" :class="[show ? 'is-active': '']">
                <div class="modal-background"></div>
                <div class="modal-card">
                    <header class="modal-card-head">
                    <p class="modal-card-title">Share your Experience</p>
                    <button class="delete" aria-label="close" @click="newTestimonial()"></button>
                    </header>
                    <section class="modal-card-body">
                        <div class="field">
                        <label class="label">On which date you recovered?</label>
                        <div class="control">
                            <date-picker v-model="testimonial.date" type="date" placeholder="DD/MM/YY"/>
                        </div>
                        </div>
                        <div class="field">
                            <label class="label">How was your experience?</label>
                            <div class="control">
                                <textarea class="textarea" v-model="testimonial.exp" placeholder="'Write in details about the experience you had when you were tested COVID possitive.'"></textarea>
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Any Suggestions for the current active patients?</label>
                            <div class="control">
                                <textarea class="textarea" v-model="testimonial.suggest" placeholder="'Motivate other possitive people ot there and suggest them some tips for speedy recovery.'"></textarea>
                            </div>
                        </div>
                    </section>
                    <footer class="modal-card-foot">
                    <button class="button is-success" @click="save()">Share</button>
                    </footer>
                </div>
            </div>
  </div>
</template>

<script>
import { getCookie } from '../main'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import axios from 'axios';

export default {
    name: "Testimonials",
    components : {
        'date-picker': DatePicker
    },
    data: function () {
        return {
            allTestimonials: [],
            testimonial: {
                exp: "",
                date: null,
                suggest: ""
            },
            show: false,
            index: 0,
            currentT: {},
            users: {},
            currentU: {}
        }
    },
    computed: {
        uid: function () {
            return getCookie('uid') || '';
        }
    },
    watch: {
        index: function () {
            if (this.index>=5) {
                this.index = 0;
            }
            this.currentT = this.allTestimonials[this.index]
            var id = this.currentT.user.$oid;
            this.currentU = this.users[id];
        }
    },
    methods: {
        newTestimonial: function () {
            this.show = !this.show;
        },
        save: function () {
            var vm = this;
            if (!vm.uid || vm.uid === '') {
                return ;
            }
            var data = {
                'rdate' : this.testimonial.date,
                'exp': this.testimonial.exp,
                'suggest': this.testimonial.suggest,
                'uid': vm.uid
            }
            axios.post('/api/v1/create/testimonial', data).then( () => {
                this.newTestimonial();
            })
        }
    },
    created: function () {
        axios.get('/api/v1/testimonials').then(resp => {
            this.allTestimonials = resp.data.data;
            this.currentT = this.allTestimonials[0];
            (this.allTestimonials).forEach((tm)=> {
                var id = tm.user.$oid || ''
                if (id !== '' && !this.users[id]){
                    axios.get('api/v1/user/' + id).then((r) => {
                        if (r.data) {
                            var u = r.data.data.data;
                            this.users[id] = u;
                            if (id === this.currentT.uid){
                                this.currentU = u;
                            }
                        }
                    })
                }
            })
        })
    },
    mounted: function () {
            this.index = 0;
            this.currentT = this.allTestimonials[this.index];
            var id = this.currentT.user.$oid;
            this.currentU = this.users[id];
            setInterval(function () {
                console.log("called");
                this.index = this.index + 1;
            }, 1000);
    }
}
</script>

<style scoped>

.box {
    width: 60%;
    margin: auto;
    margin-top: 2%;
    padding: 0px;
}

.add {
    bottom: 0px;
    width: 100%;
}

.add .box {
    width: 80%;
    margin: auto;
}

.modal-card-body {
    text-align: left;
}

.modal-card {
    margin-top: 5%;
    width: 60%;
}

.userImg {
    margin-top: 0px;
    margin-bottom: 0px;
}

.footer {
    position: absolute;
    bottom: 0px;
    width: 100%;
}

</style>