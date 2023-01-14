function doThing(event) {
    event.preventDefault();
    window.confirm('Do you want to do?') ? 
      window.location.href = '/deleteall' :
      null;
  };