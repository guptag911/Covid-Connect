<template>
  <div class="box">
      <div class="filter">
          <button class="button is-info postFilterbtnF" @click="changeTab('all-tab')" :class="currTab == 'area-tab' ? 'is-light' : ''">Posts from all India</button>
          <button class="button is-info postFilterbtnS" @click="changeTab('area-tab')" :class="currTab == 'all-tab' ? 'is-light' : ''">Posts from your area</button>
      </div>
      <loader-component v-if="isLoading" />
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
import LoaderVue from './Loader.vue'

export default {
    name: 'FeedComponent',
    components: {
        'feed-card': FeedCardVue,
        'loader-component': LoaderVue
    },
    props: {
        helpTags: Array,
        user: Object
    },
    data: function () {
        return  {
            allPosts: [],
            pageNo: 1,
            totalPages: 1,
            isLoading: false,
            currTab: 'all-tab'
        }
    },
    watch: {
        pageNo: function () {
            this.getPosts();
        },
        currTab: function () {
            this.getPosts();
        }
    },
    methods: {
        getPosts: function (myFilter = null) {
            this.isLoading = true;
            var vm = this;
            var filter = [];
            if (this.currTab === 'area-tab') {
                filter.push({
                    "type": "area",
                    "zip": vm.zip
                })
            } else {
                filter.push({});
            }
            if (myFilter) {
                filter.push(myFilter);
            }
            filter = JSON.stringify(filter)
            axios.get('/api/v1/posts/' + this.pageNo + '/' + filter).then( (resp) => {
                var data = resp.data;
                this.totalPages = Math.ceil((data.count)/10);
                this.allPosts = data.data;
                this.isLoading = false;
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
        },
        changeTab: function (tab) {
            this.currTab = tab;
            this.pageNo = 1;
        }
    },
    computed: {
        zip: function () {
            return this.user.zip || "";
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
        bus.$on('AREA_CHANGE', function (area) {
            vm.user.zip = area;
            if (vm.currTab == 'area-tab') {
                vm.pageNo = 1;
            }
        })
    }
}
</script>

<style scoped>
.box {
    background: #f0f2f5;
}

.filter {
    width: 100%;
    margin: auto;
    border: 0.5px solid #238cd1;
    border-radius: 25px;
}

.postFilterbtnF {
    width: 50%;
    border-radius: 25px 0px 0px 25px;
}

.postFilterbtnS {
    width: 50%;
    border-radius: 0px 25px 25px 0px;
}

@media screen and (max-width: 950px) {
    .box {
        padding: 5px;
    }
}
</style>