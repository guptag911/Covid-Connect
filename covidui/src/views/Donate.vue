<template>
  <div class="box">
      <h2 class="title head">Every Drop Matters!</h2>
      <div class="columns" style="padding: 5%; align-items: center">
          <div class="column">
              <div class="content">
                  <p class="title">Please share a little amount for <strong style="color: red">Covid-Help Fund</strong></p>
                  <p class="subtitle">Every last drop of the donated money will be used for proving support for families who have have lost there bread bearer, for food, animal care and whatsover help possible</p>
                  <p class="subtitle">Also the received amounts will be used for running free food champs for labour and other helpless peoples.</p>
                  <p class="subtitle">The money shall be used for proving support to family of patients who need financial help to bear the expenses of the hospitals.</p>
                  <br>
                  <br>
                  <blockquote>
                      Help others without any reason and give without the expectation of receiving anything in return.
                    <p style="text-align: right">- ROY T. BENNETT </p>
                  </blockquote>
                  <div style="align-items: center; display: flex">
                      <p>Powered By</p>
                      <div style="width: 30%">
                          <img class="image" src="https://pay.google.com/about/business/static/images/logos/logo-gp3.svg">
                      </div>
                      <div style="width: 30%"> 
                          <img  class="image" src="https://cdn.iconscout.com/icon/free/png-512/paytm-226448.png">
                      </div>
                      <div style="width: 30%">
                          <img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/UPI-Logo-vector.svg/1200px-UPI-Logo-vector.svg.png">
                      </div>
                  </div>
              </div>
          </div>
          <div class="column">
           <img class="image" src="../assets/PM-Cares-qr.png"> 
          </div>
      </div>
  </div>
</template>

<script>

export default {
    name: "DonateComponent",
}
</script>

<style scoped>
* {
    color: white;
}

.head {
    font-size: 50px;
}
.box {
    width: 100%;
    background: url('https://www.tmf-group.com/-/media/images/corporate-site/background-images/generic-website-imagery/covid19/coronavirus-1500x900.jpg');
    background-size: cover;
    text-align: left;
}

blockquote {
    background-color: #363636;
    font-weight: bolder;
    font-style: italic;
    /* color: tomato; */
}

img {
    padding: 8%;
    width: 512px;
}

</style>