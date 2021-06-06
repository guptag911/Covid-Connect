<template>
  <div class="box">
      <div v-if="allPosts.length == 0">
          <h2 class="title">No one needs help, that's great! &#128077;</h2>
      </div>
      <div v-for="post in allPosts" :key="post._id.$oid">
          <feed-card :post='post' :tags="helpTags" />
      </div>
      <hr>
    <nav class="pagination is-centered" role="navigation" aria-label="pagination">
        <a class="pagination-previous" title="This is the first page" :disabled = "isDisabled(pageNo-1)" @click="pageChange(pageNo-1)">Previous</a>
        <a class="pagination-next" :disabled = "isDisabled(pageNo+1)" @click="pageChange(pageNo+1)">Next page</a>
        <ul class="pagination-list">
            <li>
            <a class="pagination-link is-current" aria-label="Page 1" aria-current="page">{{ pageNo }}</a>
            </li>
            <li>
            <a class="pagination-link" aria-label="Goto page 'pageNo + 1'" :disabled="isDisabled(pageNo+1)"  @click="pageChange(pageNo+1)">{{ pageNo + 1 }}</a>
            </li>
            <li>
            <a class="pagination-link" aria-label="Goto page 'pageNo + 2'" :disabled="isDisabled(pageNo+2)"  @click="pageChange(pageNo+2)"> {{ pageNo + 2 }}</a>
            </li>
            <li><span class="pagination-ellipsis">&hellip;</span></li>
        </ul>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
import FeedCardVue from './FeedCard.vue'
import { bus } from '../main'

export default {
    name: 'FeedComponent',
    components: {
        'feed-card': FeedCardVue
    },
    props: {
        helpTags: Array
    },
    data: function () {
        return  {
            allPosts: [],
            pageNo: 1,
            totalPages: 1
        }
    },
    watch: {
        pageNo: function () {
            this.getPosts();
        }
    },
    methods: {
        getPosts: function () {
            axios.get('/api/v1/posts/' + this.pageNo).then( (resp) => {
                var data = resp.data;
                this.totalPages = Math.ceil((data.count)/10);
                this.allPosts = data.data;
            })
        },
        isDisabled: function (page){
            if (page <= 0){
                return true;
            }
            if (page > this.totalPages) {
                return true;
            }
            return false;
        },
        pageChange: function (page) {
            if (this.isDisabled(page)){
                return;
            }
            this.pageNo = page;
        }
    },
    mounted: function () {
        this.getPosts();
        var vm = this;
        bus.$on('NEW_POST_ADDED', function () {
            if (vm.pageNo === 1){
                vm.getPosts();
            }
        })
    }
}
</script>

<style scoped>
.box {
    background: #f0f2f5;
}
</style>