<template>
	<div>
		<div class="main">
			<router-link to="/dashboard">
				<button
					class="button is-link is-light"
					style="width: 100%; margin-bottom: 2%;"
				>
					Back
				</button>
			</router-link>
			<div class="tabChanger">
				<button class="button" :class="currTab == 'edit' ? 'is-active': 'is-inactive'"  @click="tabChange('edit')">
					Profile
				</button>
				<button class="button" :class="currTab == 'posts' ? 'is-active': 'is-inactive'"  @click="tabChange('posts')">
					Posts
				</button>
			</div>
			<div class="box">
				<div class="display">
					<div v-if="currTab == 'edit'">
						<edit-profile />
					</div>
					<div v-if="currTab == 'posts'">
						<span v-if="allPosts.length > 0">
							<span  v-for="(post, i) in allPosts" :key="i">
							<feed-card
								:post="post"
								:tags="helpTags"
								:isAdmin="true"
							/>
						</span>
						<nav
							class="pagination is-centered"
							role="navigation"
							aria-label="pagination"
						>
							<a
								class="pagination-previous"
								title="This is the first page"
								:disabled="isDisabled(pageNo - 1)"
								@click="pageChange(pageNo - 1)"
								>Previous</a
							>
							<a
								class="pagination-next"
								:disabled="isDisabled(pageNo + 1)"
								@click="pageChange(pageNo + 1)"
								>Next page</a
							>
							<ul class="pagination-list">
								<li>
									<a
										class="pagination-link is-current"
										aria-label="Page 1"
										aria-current="page"
										>{{ pageNo }}</a
									>
								</li>
								<li>
									<a
										class="pagination-link"
										aria-label="Goto page 'pageNo + 1'"
										:disabled="isDisabled(pageNo + 1)"
										@click="pageChange(pageNo + 1)"
										>{{ pageNo + 1 }}</a
									>
								</li>
								<li>
									<a
										class="pagination-link"
										aria-label="Goto page 'pageNo + 2'"
										:disabled="isDisabled(pageNo + 2)"
										@click="pageChange(pageNo + 2)"
									>
										{{ pageNo + 2 }}</a
									>
								</li>
								<li>
									<span class="pagination-ellipsis"
										>&hellip;</span
									>
								</li>
							</ul>
						</nav>
						</span>
						<span v-else>
							<h2>You haven't added any posts yet!</h2>
						</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from "axios";
	import EditProfile from "../components/EditProfile.vue";
	import FeedCardVue from "../components/FeedCard.vue";
	import { bus } from "../main";
	export default {
		components: {
			"edit-profile": EditProfile,
			"feed-card": FeedCardVue,
		},
		name: "UserProfile",
		data: function() {
			return {
				currTab: "edit",
				allPosts: [],
				pageNo: 1,
				isLoading: false,
				totalPages: 0,
				helpTags: [
					{
						id: 0,
						label: "Need Blood",
						desc:
							"This category covers all the blood related requests, like you need blood. Please do spectify the blood group in title.",
					},
					{
						id: 1,
						label: "Pet Service",
						desc:
							"This category covers pet related help, like pet care, pet medical services, etc.",
					},
					{
						id: 2,
						label: "Food Service",
						desc:
							"This category covers food related help needed, like free food at doorstep, etc.",
					},
					{
						id: 3,
						label: "Medical Help",
						desc:
							"This category covers any medical help that you may need, like updating medicine stocks, etc.",
					},
					{
						id: 10,
						label: "Others",
						desc:
							"This category covers all the other kind of help that you want. Please desribe clearly the help you need.",
					},
				],
			};
		},
		computed: {
			uid: function() {
				return this.$route.query.id || "";
			},
		},
		watch: {
			currTab: function() {
				if (this.currTab === "posts") {
					this.pageNo = 1;
					this.getPosts();
				}
			},
			pageNo: function() {
				this.getPosts();
			},
		},
		methods: {
			tabChange: function(tab) {
				this.currTab = tab;
			},
			getPosts: function() {
				var query = [
					{
						type: "mine",
						id: this.uid,
					},
				];
				query = JSON.stringify(query);
				if (this.currTab === "posts") {
					axios
						.get("/api/v1/posts/" + this.pageNo + "/" + query)
						.then((resp) => {
							var data = resp.data;
							this.totalPages = Math.ceil(data.count / 10);
							this.allPosts = data.data;
							this.isLoading = false;
						});
				}
			},
			isDisabled: function(page) {
				if (page <= 0) {
					return true;
				}
				if (page > this.totalPages) {
					return true;
				}
				return false;
			},
			pageChange: function(page) {
				if (this.isDisabled(page)) {
					return;
				}
				this.pageNo = page;
			},
		},
		mounted: function() {
			var vm = this;
			bus.$on("POST_DELETED", function() {
				vm.getPosts();
			});
		},
	};
</script>

<style scoped>
	.main {
		top: 15px;
		margin: 10%;
		padding: 0px;
		margin-top: 6%;
	}

	.box {
		padding: 1%;
	}

	.tabs {
		display: block;
		text-align: left;
	}

	.tabs button {
		width: 100%;
		border-radius: 0px;
		display: block;
	}
	.display {
		margin-right: 1%;
	}

	.tabChanger {
		text-align: left;
		width: 100%;
		margin-bottom: 0px;
	}
	.tabChanger button {
		width: 25%;
		background: #3273dc;
		margin-right: 2px;
		color: white;
	}
	.is-active {
		background: #2160c4 !important;
		font-weight: bold;
		transform: scale(1.1);
	}
	.is-inactive {
		background: whitesmoke !important;
		border-color: #273d51;
		color: #273d51 !important;
	}
	@media screen and (max-width: 950px) {
		.main {
			margin: 2%;
		}
	}
</style>
