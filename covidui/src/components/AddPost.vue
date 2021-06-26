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
        <button v-if="!isNewPost" class="button is-info createbtn is-medium" style="background-color: #2160c4" @click="toggleNewPost">Create Post</button>
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
                <span class="button is-link" style="width: 48%; margin: 0.5%;" @click="onCreate()">Create</span>
                <span class="button is-link" style="width: 48%; margin: 0.5%;" @click="toggleNewPost">Cancel</span>
            </div>
        </div>
    </div>
</template>

<script>
import { VueEditor } from "vue2-editor";
import Multiselect from 'vue-multiselect'
import axios from 'axios';
import {bus} from '../main'

export default {
    name: 'AddPostComponent',
    props: {
        id: String,
        helpTags: Array
    },
    data: function () {
        return {
            postInput: {
                desc: "",
                title: "",
                tag: null
            },
            isNewPost: false,
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
                    this.postInput.title = "",
                    this.postInput.tag = null;
                    this.postInput.desc = "";
                    bus.$emit('NEW_POST_ADDED');
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

    .box {
        text-align: left;
    }
    .title {
        text-align: center;
    }
    .help {
        color: gray;
    }

    .ql-editing {
        position: relative !important;
        top: 0px !important;
        left: 0px !important;
    }
</style>