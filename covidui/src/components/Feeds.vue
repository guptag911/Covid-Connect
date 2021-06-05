<template>
    <div class="feedMain">
        <div
            class="notification"
            v-if="isError || isSuccess"
            :class="isError ? 'is-danger' : 'is-success'"
        >
            <button class="delete" @click="hideNotification()"></button>
            {{ errorMsg }}
        </div>
        <button v-if="!isNewPost" class="button is-info createbtn is-medium" @click="toggleNewPost">Create Post</button>
        <div v-if="isNewPost" class="box">
            <p class="title">Don't worry we are with you!</p>
            <div class="field">
                <label class="label">Title</label>
                <div class="control">
                    <input class="input" type="text" placeholder="Help title" v-model="postInput.title">
                </div>
            </div>
            <div class="field">
                <label class="label">Category</label>
                <div class="control">
                    <vue-multiselect :options="helpTags" v-model="postInput.tag" tracBy="id" label="label" placeholder="Select the caterogry of help you want."/>
                    <span v-if="postInput.tag" class="help">{{ postInput.tag.desc }}</span>
                </div>
            </div>
            <div class="field">
                <label class="label">Discription</label>
                <div class="control">
                    <vue-editor v-model="postInput.desc" :placeholder="'Write in details the help you need.'" />
                </div>
            </div>
            <div style="text-align: center;">
                <span class="button is-info" style="width: 48%; margin: 0.5%;" @click="onCreate()">Create</span>
                <span class="button is-info" style="width: 48%; margin: 0.5%;" @click="toggleNewPost">Cancel</span>
            </div>
        </div>
    </div>
</template>

<script>
import { VueEditor } from "vue2-editor";
import Multiselect from 'vue-multiselect'
import axios from 'axios';

export default {
    name: 'FeedsComponent',
    props: {
        id: String
    },
    data: function () {
        return {
            postInput: {
                desc: "",
                title: "",
                tag: null
            },
            isNewPost: false,
            helpTags: [
                {
                    id: 0,
                    label: "Need Blood",
                    desc: "This category covers all the blood related requests, like you need blood. Please do spectify the blood group in title."
                },
                {
                    id: 1,
                    label: "Pet Service",
                    desc: "This category covers pet related help, like pet care, pet medical services, etc."
                },
                {
                    id: 2,
                    label: "Food Service",
                    desc: "This category covers food related help needed, like free food at doorstep, etc."

                },
                {
                    id: 3,
                    label: "Medical Help",
                    desc: "This category covers any medical help that you may need, like updating medicine stocks, etc."

                },
                {
                    id: 10,
                    label: "Others",
                    desc: "This category covers all the other kind of help that you want. Please desribe clearly the help you need."
                }
            ],
            isError: false,
            errorMsg: "",
            isSuccess: false
        }
    },
    components: {
        'vue-editor': VueEditor,
        'vue-multiselect': Multiselect,
    },
    methods: {
        toggleNewPost: function () {
            this.isNewPost = !this.isNewPost;
        },
        performValidations: function () {
            if (this.postInput.title.length === 0) {
                this.isError = true;
                this.errorMsg = "Please Enter a title"
                return false;
            }
            return true;
        },
        onCreate: function () {
            if (!this.performValidations()) { return }
            if (this.postInput.tag === null || this.postInput.tab === {}) {
                this.postInput.tag = 10
            } else {
                this.postInput.tag = this.postInput.tag.id
            }
            this.postInput.user = this.id;
            axios.post('/api/v1/posts', this.postInput).then( (resp) => {
                if (resp.data.status !== 200){
                    this.isError = true;
                    this.errorMsg = "Some Error Occured!"
                } else {
                    setInterval(this.hideNotification, 2000);
                    this.isSuccess = true;
                    this.errorMsg = "Post Succesfully Created";
                    this.isNewPost = false;   
                }
            })
        },
        hideNotification: function () {
            this.isError = false;
            this.isSuccess = false;
            this.errorMsg = "";
        }
    }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
    @import "~vue2-editor/dist/vue2-editor.css";

    .createbtn {
        width: 100%;
    }
    .feedMain {
        margin: 1%;
        margin-left: 0px;
        padding-top: 0.5px;
    }

    .box {
        text-align: left;
    }
    .title {
        text-align: center;
    }
    .help {
        color: gray;
    }
</style>