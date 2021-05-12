const fs = require('fs')
const path = require('path')

const INPUT_DIR = '../build/contracts'
const OUTPUT_DIR = '../prepared/contracts'

function prepare_abi(contractJSON) {
  const contractMeta = JSON.parse(contractJSON);
  const { abi } = contractMeta;

  const preparedMeta = abi.map(description => {
    if(description.type === "function"
     && description.gas) {
      description.gas = undefined;
    }
    
    return description
  })

  return JSON.stringify(preparedMeta, null, 2)
}

async function main() {
  const inputDir = path.join(__dirname, INPUT_DIR)
  const outputDir = path.join(__dirname, OUTPUT_DIR)
  
  const contract_filenames = fs.readdirSync(inputDir).filter(fn => fn.endsWith('.json'));

  if (!fs.existsSync(outputDir)){
    fs.mkdirSync(outputDir, { recursive: true });
  }
  contract_filenames.map(contract_filename => {
    const contract = fs.readFileSync(path.join(inputDir, contract_filename))
    const preparedContract = prepare_abi(contract)
    fs.writeFileSync(path.join(outputDir, contract_filename), preparedContract)
  })
}

main()