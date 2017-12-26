<template>
  <div class="main">
    <div class="container">
      <div class="card">
        <h1>Opgenomen</h1>
        <ul class="list-group">
          <li class="list-group-item textleft">
            <span class="badge badge-primary badge-pill">datum</span>
            <span class="left">Dapibus ac facilisis in</span>
            <a class="right actionbuttons"><i class="fa fa-plus fa-2x" aria-hidden="true"></i></a>
            <a class="right actionbuttons"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
          <li class="list-group-item textleft">
            <span class="badge badge-primary badge-pill right">datum</span>
            <span class="left">Dapibus ac facilisis in</span>
            <a class="right actionbuttons"><i class="fa fa-plus fa-2x" aria-hidden="true"></i></a>
            <a class="right actionbuttons"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
          <li class="list-group-item textleft act">
            <span class="badge badge-primary badge-pill right">datum</span>
            <span class="left">Dapibus ac facilisis in</span>
            <a class="right actionbuttons white"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
        </ul>
        <nav aria-label="Page navigation example">
          <ul class="pagination justify-content-end">
            <li class="page-item disabled">
              <a class="page-link" href="#" tabindex="-1">Vorige</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
              <a class="page-link" href="#">Volgende</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="card">
        <h1>Afspeellijst</h1>
         <ul class="list-group">
          <li class="list-group-item textleft act">
            <span class="badge badge-primary badge-pill right">datum</span>
            <span class="left">Dapibus ac facilisis in</span>
            <a class="right actionbuttons white"><i class="fa fa-minus fa-2x" aria-hidden="true"></i></a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {

    }
  }
}
</script>
