/*Для того, чтобы гранулярно настроить 
карусель, недостаточно просто добавить её 
на страницу. Придётся инициализировать её 
вручную, задав нужные параметры. Для этого 
нам надо убрать параметр data-ride из 
внешнего дива, и тогда мы можем использовать
id карусели и в нашей функции инциализации
 по загрузке документа, добавив следующий
  код: $("#my-carousel").carousel();*/

  $("#carouselWithIndicators").carousel({
  interval: 625
})$("#carouselWithIndicators").carousel({wrap: false});
  // отключение автоматической перемотки карусели