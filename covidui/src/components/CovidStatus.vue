<template>
    <div class="box">
        <div class="user-img">
            <figure class="image is-128x128">
                <img class="is-rounded" src="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551">
            </figure>
        </div>
        <h3 class="head">India Covid Statistics</h3>
        <hr>
        <div style="width: 90%; text-align: center;">    
            <span class="card box" style="text-align: center; background: gold">
                <header>
                    <p class="head">
                    Active Cases
                    </p>
                </header>
                <div class="card-content">
                    <div class="content">
                    {{ active }}
                    </div>
                </div>
            </span>
            <span class="card box" style="text-align: center; background: #ff5b5bc9">
                <header>
                    <p class="head">
                    Total Deaths
                    </p>
                </header>
                <div class="card-content">
                    <div class="content">
                    {{ deaths }}
                    </div>
                </div>
            </span>
            <span class="card box" style="text-align: center; background: greenyellow">
                <header>
                    <p class="head">
                    Total Cured
                    </p>
                </header>
                <div class="card-content">
                    <div class="content">
                    {{ cured }}
                    </div>
                </div>
            </span>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default{
    name: 'CovidStatus',
    data: function () {
        return {
            active: 0,
            deaths: 0,
            cured: 0
        }
    },
    mounted: function () {
        axios.get('https://www.mohfw.gov.in/data/datanew.json').then((resp) => {
            var stats = resp.data;
            var l = stats.length - 1;
            var indiaStats = stats[l];
            this.active = indiaStats.new_active;
            this.deaths = indiaStats.new_death;
            this.cured = indiaStats.new_cured;
        })
    }
}
</script>

<style scoped>
.box {
    text-align: left;
    margin: 2%;
    width: 100%;
}

.user-img {
    text-align: -webkit-center;
}

.head {
    text-align: center;
    font-weight: bolder;
}

.mycard {
    text-align: center;
    background-color: blue;
}

.content {
    font-size: x-large;
}
</style>