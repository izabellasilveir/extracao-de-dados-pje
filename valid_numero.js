function validarNumeroUnicoProcesso(numero) {
    const bcmod = (x, y) =>
    {
      const take = 5;
      let mod = '';
  
      do
      {
        let a = parseInt(mod + x.substr(0, take));
        x = x.substr(take);
        mod = a % y;
      }
      while (x.length);
  
      return mod;
    };
  
    // remove todos os pontos e traços
    const numeroProcesso = numero.replace(/[.-]/g, '')
  
    if (numeroProcesso.length < 14 || isNaN(numeroProcesso)) {
      return false;
    }
  
    const digitoVerificadorExtraido = parseInt(numeroProcesso.substr(-13, 2));
  
    const vara = numeroProcesso.substr(-4, 4);  // (4) vara originária do processo
    const tribunal = numeroProcesso.substr(-6, 2);  // (2) tribunal
    const ramo = numeroProcesso.substr(-7, 1);  // (1) ramo da justiça
    const anoInicio = numeroProcesso.substr(-11, 4);  // (4) ano de inicio do processo
    const tamanho = numeroProcesso.length - 13;
    const numeroSequencial = numeroProcesso.substr(0, tamanho).padStart(7, '0');  // (7) numero sequencial dado pela vara ou juizo de origem
  
    const digitoVerificadorCalculado = 98 - bcmod((numeroSequencial + anoInicio + ramo + tribunal + vara + '00'), '97');
  
    console.log(digitoVerificadorExtraido)
    console.log(digitoVerificadorCalculado)
    return digitoVerificadorExtraido === digitoVerificadorCalculado;

}

validarNumeroUnicoProcesso("1063417-92.2011.8.06.0001")