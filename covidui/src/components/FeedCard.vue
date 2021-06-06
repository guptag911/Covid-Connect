<template>
    <div class="headCard"> 
        <div class="box postCard">
            <span class="is-size-7">{{ date }}</span>
            <article class="media">
                <div class="media-content">
                    <div class="content">
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
        <button v-if="!showDetails" class="button is-dark is-fullwidth is-fullwidth" :class="isLoading ? 'is-loading' : ''" @click="togglePostCreate()">Contact for Help</button>
        <button v-if="showDetails" class="button is-dark is-fullwidth is-fullwidth" :class="isLoading ? 'is-loading' : ''" @click="togglePostCreate ()">Hide Details!</button>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'FeedCardComponent',
    props: {
        post: Object,
        tags: Array
    },
    data: function () {
        return {
            isLoading: false,
            postTag: "",
            date: "",
            postCreater: null,
            showDetails: false
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
</style>