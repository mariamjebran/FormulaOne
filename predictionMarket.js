const PredictionMarket = artifacts.require('PredictionMarket.sol');
  
const Side = {
  Verstappen: 0,
  Leclerc: 1,
  Perez: 2,
  Russel: 3,
  Sainz: 4,
  Other: 5
};

contract('PredictionMarket', addresses => {
  const [admin, oracle, gambler1, gambler2, gambler3, gambler4, gambler5, gambler6, _] = addresses;

  it('should work', async () => {
    const predictionMarket = await PredictionMarket.new(oracle);
    
    await predictionMarket.placeBet(
      Side.Verstappen, 
      {from: gambler1, value: web3.utils.toWei('1')}
    );
    await predictionMarket.placeBet(
      Side.Leclerc, 
      {from: gambler2, value: web3.utils.toWei('1')}
    );
    await predictionMarket.placeBet(
      Side.Perez, 
      {from: gambler3, value: web3.utils.toWei('1')}
    );
    await predictionMarket.placeBet(
      Side.Russel, 
      {from: gambler4, value: web3.utils.toWei('1')}
    );
    await predictionMarket.placeBet(
      Side.Sainz, 
      {from: gambler5, value: web3.utils.toWei('1')}
    );
    await predictionMarket.placeBet(
      Side.Other, 
      {from: gambler6, value: web3.utils.toWei('1')}
    );

    await predictionMarket.reportResult(
      Side.Verstappen,
      Side.Leclerc,
      Side.Perez,
      Side.Russel,
      Side.Sainz,
      Side.Other,
      {from: oracle}
    );

    const balancesBefore = (await Promise.all( 
      [gambler1, gambler2, gambler3, gambler4, gambler5, gambler6].map(gambler => (
        web3.eth.getBalance(gambler)
      ))
    ))
    .map(balance => web3.utils.toBN(balance));
    await Promise.all(
      [gambler1].map(gambler => (
        predictionMarket.withdrawGain({from: gambler})
      ))
    );
    const balancesAfter = (await Promise.all( 
      [gambler1, gambler2, gambler3, gambler4, gambler5, gambler6].map(gambler => (
        web3.eth.getBalance(gambler)
      ))
    ))
    .map(balance => web3.utils.toBN(balance));

    //gambler 1, 2, 3 should have respectively 2, 2 and 4 extra ether
    //but we also have to take into consideration gas spent when calling
    //withdrawGain(). We can ignore this problem by just comparing
    //the first 3 digits of balances
    assert(balancesAfter[0].sub(balancesBefore[0]).toString().slice(0, 3) === '599');
    assert(balancesAfter[1].sub(balancesBefore[1]).isZero());
    assert(balancesAfter[2].sub(balancesBefore[2]).isZero());
    assert(balancesAfter[3].sub(balancesBefore[3]).isZero());
    assert(balancesAfter[4].sub(balancesBefore[4]).isZero());
    assert(balancesAfter[5].sub(balancesBefore[5]).isZero());
    
  });
});