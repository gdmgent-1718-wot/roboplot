<template>
  <div id="app">
    <header>
      <span class="title">RoboPlot</span>
    </header>
    <main>
      <hello></hello>
    </main>
  </div>
</template>

<script>
import Hello from './components/Hello'

export default {
  name: 'app',
  components: {
    Hello
  }
}
</script>