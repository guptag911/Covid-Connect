<template>
    <div class="headCard"> 
        <div class="box postCard">
            <span class="is-size-7">{{ date }}</span>
            <span v-if="isAdmin" @click="toggleDeleteBox()"><i class="fas fa-trash-alt"></i></span>
            <div v-if="showDelBox" class="box confirmation">
                <p>Are you sure, you want to delete this post? </p>
                <button class="button is-danger" @click="deletePost()">Yes</button>
                <button class="button is-success is-light" @click="toggleDeleteBox()">No</button>
            </div>
            <article class="media">
                <div class="media-content">
                    <div class="content" style="overflow: auto;">
                    <p>
                        <strong class="title">{{ post.title }}</strong>
                        <br>
                        <span v-html="post.desc"></span>
                    </p>
                    </div>
                </div>
                <div class="media-right">
                    <span class="tag is-danger" style="border-radius: 15px">{{ postTag }}</span>
                </div>
            </article>
            <div v-if="showDetails" class="content">
                <hr>
                    <h5>Name: {{ postCreater.name }}</h5>
                    <h5>Email: {{ postCreater.email}}</h5>
                    <h5>Mobile: {{ postCreater.number }}</h5>
            </div>
        </div>
        <button v-if="!showDetails && !isAdmin" class="button is-dark is-fullwidth is-fullwidth" :class="isLoading ? 'is-loading' : ''" @click="togglePostCreate()">Contact for Help</button>
        <button v-if="showDetails" class="button is-dark is-fullwidth is-fullwidth" :class="isLoading ? 'is-loading' : ''" @click="togglePostCreate ()">Hide Details!</button>
    </div>
</template>

<script>
import axios from 'axios';
import { bus } from '../main';
export default {
    name: 'FeedCardComponent',
    props: {
        post: Object,
        tags: Array,
        isAdmin: {
            default: false,
            type: Boolean
        }
    },
    data: function () {
        return {
            isLoading: false,
            postTag: "",
            date: "",
            postCreater: null,
            showDetails: false,
            showDelBox: false
        }
    },
    methods: {
        togglePostCreate: function () {
            if (!this.postCreater) {
                this.getPostCreater();
            }
            this.showDetails = !this.showDetails;
        },
        getTagData: function () {
            var tag = this.post.tag;
            for(var i = 0; i < (this.tags).length ; i++) {
                if (this.tags[i].id == tag) {
                    this.postTag = this.tags[i].label;
                    break;
                }
            }
        },
        parseCreatedDate: function () {
            if (this.post  && this.post.createdAt && this.post.createdAt.$date) {
                var timestamp = this.post.createdAt.$date;
                var x =  new Date(timestamp).toLocaleString();
                this.date = x;
            }
            return ''
        },
        getPostCreater: function () {
            this.isLoading = true;
            var uid = ""
            if (this.post.user && this.post.user.$oid) {
                uid = this.post.user.$oid;
            }
            axios.get('/api/v1/user/' + uid).then((resp) => {
                if (resp.status == 200) {
                    this.isLoading = false;
                    this.postCreater = resp.data.data.data;
                } else {
                    this.isLoading = false;
                    this.postCreater = null;
                }
            })
        },
        toggleDeleteBox: function () {
            this.showDelBox = !this.showDelBox;
        },
        deletePost: function () {
            var id = this.post && this.post._id && this.post._id.$oid;
            var payload = {
                'id' : id
            }
            axios.post('/api/v1/delete/post', payload).then((resp) => {
                if (resp.data.status == 200) {
                    this.toggleDeleteBox();
                    bus.$emit('POST_DELETED');
                }
            })
        }
    },
    mounted: function () {
        this.getTagData();
        this.parseCreatedDate();
    }
}
</script>

<style scoped>
.postCard {
    margin: 2px;
    margin-bottom: 0%;
}

.headCard {
    margin: 2%;
    border: 0.5px solid grey;
    border-radius: 8px;
}

.details {
    margin: 2px;
}

i {
    right: 2%;
    position: absolute;
}

.confirmation {
    width: 60%;
    padding: 3%;
    margin: 0px;
    right: -20%;
    position: absolute;
    background: whitesmoke;
    text-align: center;
    font-weight: bold;
}

.confirmation button {
    width: 40%;
    margin: 3px;
}
</style>