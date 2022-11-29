from quiz_app_teacher.models import *
from quiz_app_student.models import *
from accounts.models import *
import random
words=['a', 'aa', 'aaa', 'aaron', 'ab', 'abandoned', 'abc', 'aberdeen', 'abilities','ability', 'able', 'aboriginal', 'abortion', 'about', 'above', 'abraham', 'abroad', 'abs', 'absence', 'absent', 'absolute', 'absolutely', 'absorption', 'abstract', 'abstracts', 'abu', 'abuse', 'ac', 'academic', 'academics', 'academy', 'acc', 'accent', 'accept', 'acceptable', 'acceptance', 'accepted', 'accepting', 'accepts', 'access', 'accessed', 'accessibility', 'accessible', 'accessing', 'accessories', 'accessory', 'accident', 'accidents', 'accommodate', 'accommodation', 'accommodations', 'accompanied', 'accompanying', 'accomplish', 'accomplished', 'accordance', 'according', 'accordingly', 'account', 'accountability', 'accounting', 'accounts', 'accreditation', 'accredited', 'accuracy', 'accurate', 'accurately', 'accused', 'acdbentity', 'ace', 'acer', 'achieve', 'achieved', 'achievement', 'achievements', 'achieving', 'acid', 'acids', 'acknowledge', 'acknowledged', 'acm', 'acne', 'acoustic', 'acquire', 'acquired', 'acquisition', 'acquisitions', 'acre', 'acres', 'acrobat', 'across', 'acrylic', 'act', 'acting', 'action', 'actions', 'activated', 'activation', 'active', 'actively', 'activists', 'activities', 'activity', 'actor', 'actors', 'actress', 'acts', 'actual', 'actually', 'acute', 'ad', 'ada', 'adam', 'adams', 'adaptation', 'adapted', 'adapter', 'adapters', 'adaptive', 'adaptor', 'add', 'added', 'addiction', 'adding', 'addition', 'additional', 'additionally', 'additions', 'address', 'addressed', 'addresses', 'addressing', 'adds', 'adelaide', 'adequate', 'adidas', 'adipex', 'adjacent', 'adjust', 'adjustable', 'adjusted', 'adjustment', 'adjustments', 'admin', 'administered', 'administration', 'administrative', 'administrator', 'administrators', 'admission', 'admissions', 'admit', 'admitted', 'adobe', 'adolescent', 'adopt', 'adopted', 'adoption', 'adrian', 'ads', 'adsl', 'adult', 'adults', 'advance', 'advanced', 'advancement', 'advances', 'advantage', 'advantages', 'adventure', 'adventures', 'adverse', 'advert', 'advertise', 'advertisement', 'advertisements', 'advertiser', 'advertisers', 'advertising', 'advice', 'advise', 'advised', 'advisor', 'advisors', 'advisory', 'advocacy', 'advocate', 'adware', 'ae', 'aerial', 'aerospace', 'af', 'affair', 'affairs', 'affect', 'affected', 'affecting', 'affects', 'affiliate', 'affiliated', 'affiliates', 'affiliation', 'afford', 'affordable', 'afghanistan', 'afraid', 'africa', 'african', 'after', 'afternoon', 'afterwards', 'ag', 'again', 'against', 'age', 'aged', 'agencies', 'agency', 'agenda', 'agent', 'agents', 'ages', 'aggregate', 'aggressive', 'aging', 'ago', 'agree', 'agreed', 'agreement', 'agreements', 'agrees', 'agricultural', 'agriculture', 'ah', 'ahead', 'ai', 'aid', 'aids', 'aim', 'aimed', 'aims', 'air', 'aircraft', 'airfare', 'airline', 'airlines', 'airplane', 'airport', 'airports', 'aj', 'ak', 'aka', 'al', 'ala', 'alabama', 'alan', 'alarm', 'alaska', 'albania', 'albany', 'albert', 'alberta', 'album', 'albums', 'albuquerque', 'alcohol', 'alert', 'alerts', 'alex', 'alexander', 'alexandria', 'alfred', 'algebra', 'algeria', 'algorithm', 'algorithms', 'ali', 'alias', 'alice', 'alien', 'align', 'alignment', 'alike', 'alive', 'all', 'allah', 'allan', 'alleged', 'allen', 'allergy', 'alliance', 'allied', 'allocated', 'allocation', 'allow', 'allowance', 'allowed', 'allowing', 'allows', 'alloy', 'almost', 'alone', 'along', 'alot', 'alpha', 'alphabetical', 'alpine', 'already', 'also', 'alt', 'alter', 'altered', 'alternate', 'alternative', 'alternatively', 'alternatives', 'although', 'alto', 'aluminium', 'aluminum', 'alumni', 'always', 'am', 'amanda', 'amateur', 'amazing', 'amazon', 'amazoncom', 'amazoncouk', 'ambassador', 'amber', 'ambien', 'ambient', 'amd', 'amend', 'amended', 'amendment', 'amendments', 'amenities', 'america', 'american', 'americans', 'americas', 'amino', 'among', 'amongst', 'amount', 'amounts', 'amp', 'ampland', 'amplifier', 'amsterdam', 'amy', 'an', 'ana', 'anaheim', 'anal', 'analog', 'analyses', 'analysis', 'analyst', 'analysts', 'analytical', 'analyze', 'analyzed', 'anatomy', 'anchor', 'ancient', 'and', 'andale', 'anderson', 'andorra', 'andrea', 'andreas', 'andrew', 'andrews', 'andy', 'angel', 'angela', 'angeles', 'angels', 'anger', 'angle', 'angola', 'angry', 'animal', 'animals', 'animated', 'animation', 'anime', 'ann', 'anna', 'anne', 'annex', 'annie', 'anniversary', 'annotated', 'annotation', 'announce', 'announced', 'announcement', 'announcements', 'announces', 'annoying', 'annual', 'annually', 'anonymous', 'another', 'answer', 'answered', 'answering', 'answers', 'ant', 'antarctica', 'antenna', 'anthony', 'anthropology', 'anti', 'antibodies', 'antibody', 'anticipated', 'antigua', 'antique', 'antiques', 'antivirus', 'antonio', 'anxiety', 'any', 'anybody', 'anymore', 'anyone', 'anything', 'anytime', 'anyway', 'anywhere', 'aol', 'ap', 'apache', 'apart', 'apartment', 'apartments', 'api', 'apnic', 'apollo', 'app', 'apparatus', 'apparel', 'apparent', 'apparently', 'appeal', 'appeals', 'appear', 'appearance', 'appeared', 'appearing', 'appears', 'appendix', 'apple', 'appliance', 'appliances', 'applicable', 'applicant', 'applicants', 'application', 'applications', 'applied', 'applies', 'apply', 'applying', 'appointed', 'appointment', 'appointments', 'appraisal', 'appreciate', 'appreciated', 'appreciation', 'approach', 'approaches', 'appropriate', 'appropriations', 'approval', 'approve', 'approved', 'approx', 'approximate', 'approximately', 'apps', 'apr', 'april', 'apt', 'aqua', 'aquarium', 'aquatic', 'ar', 'arab', 'arabia', 'arabic', 'arbitrary', 'arbitration', 'arc', 'arcade', 'arch', 'architect', 'architects', 'architectural', 'architecture', 'archive', 'archived', 'archives', 'arctic', 'are', 'area', 'areas', 'arena', 'arg', 'argentina', 'argue', 'argued', 'argument', 'arguments', 'arise', 'arising', 'arizona', 'arkansas', 'arlington', 'arm', 'armed', 'armenia', 'armor', 'arms', 'armstrong', 'army', 'arnold', 'around', 'arrange', 'arranged', 'arrangement', 'arrangements', 'array', 'arrest', 'arrested', 'arrival', 'arrivals', 'arrive', 'arrived', 'arrives', 'arrow', 'art', 'arthritis', 'arthur', 'article', 'articles', 'artificial', 'artist', 'artistic', 'artists', 'arts', 'artwork', 'aruba', 'as', 'asbestos', 'ascii', 'ash', 'ashley', 'asia', 'asian', 'aside', 'asin', 'ask', 'asked', 'asking', 'asks', 'asn', 'asp', 'aspect', 'aspects', 'aspnet', 'ass', 'assault', 'assembled', 'assembly', 'assess', 'assessed', 'assessing', 'assessment', 'assessments', 'asset', 'assets', 'assign', 'assigned', 'assignment', 'assignments', 'assist', 'assistance', 'assistant', 'assisted', 'assists', 'associate', 'associated', 'associates', 'association', 'associations', 'assume', 'assumed', 'assumes', 'assuming', 'assumption', 'assumptions', 'assurance', 'assure', 'assured', 'asthma', 'astrology', 'astronomy', 'asus', 'at', 'ata', 'ate', 'athens', 'athletes', 'athletic', 'athletics', 'ati', 'atlanta', 'atlantic', 'atlas', 'atm', 'atmosphere', 'atmospheric', 'atom', 'atomic', 'attach', 'attached', 'attachment', 'attachments', 'attack', 'attacked', 'attacks', 'attempt', 'attempted', 'attempting', 'attempts', 'attend', 'attendance', 'attended', 'attending', 'attention', 'attitude', 'attitudes', 'attorney', 'attorneys', 'attract', 'attraction', 'attractions', 'attractive', 'attribute', 'attributes', 'au', 'auburn', 'auckland', 'auction', 'auctions', 'aud', 'audi', 'audience', 'audio', 'audit', 'auditor', 'aug', 'august', 'aurora', 'aus', 'austin', 'australia', 'australian', 'austria', 'authentic', 'authentication', 'author', 'authorities', 'authority', 'authorization', 'authorized', 'authors', 'auto', 'automated', 'automatic', 'automatically', 'automation', 'automobile', 'automobiles', 'automotive', 'autos', 'autumn', 'av', 'availability', 'available', 'avatar', 'ave', 'avenue', 'average', 'avg', 'avi', 'aviation', 'avoid', 'avoiding', 'avon', 'aw', 'award', 'awarded', 'awards', 'aware', 'awareness', 'away', 'awesome', 'awful', 'axis', 'aye', 'az', 'azerbaijan', 'b', 'ba', 'babe', 'babes', 'babies', 'baby', 'bachelor', 'back', 'backed', 'background', 'backgrounds', 'backing', 'backup', 'bacon', 'bacteria', 'bacterial', 'bad', 'badge', 'badly', 'bag', 'baghdad', 'bags', 'bahamas', 'bahrain', 'bailey', 'baker', 'baking', 'balance', 'balanced', 'bald', 'bali', 'ball', 'ballet', 'balloon', 'ballot', 'balls', 'baltimore', 'ban', 'banana', 'band', 'bands', 'bandwidth', 'bang', 'bangbus', 'bangkok', 'bangladesh', 'bank', 'banking', 'bankruptcy', 'banks', 'banned', 'banner', 'banners', 'baptist', 'bar', 'barbados', 'barbara', 'barbie', 'barcelona', 'bare', 'barely', 'bargain', 'bargains', 'barn', 'barnes', 'barrel', 'barrier', 'barriers', 'barry', 'bars', 'base', 'baseball', 'based', 'baseline', 'basement', 'basename', 'bases', 'basic', 'basically', 'basics', 'basin', 'basis', 'basket', 'basketball', 'baskets', 'bass', 'bat', 'batch', 'bath', 'bathroom', 'bathrooms', 'baths', 'batman', 'batteries', 'battery', 'battle', 'battlefield', 'bay', 'bb', 'bbc', 'bbs', 'bbw', 'bc', 'bd', 'bdsm', 'be', 'beach', 'beaches', 'beads', 'beam', 'bean', 'beans', 'bear', 'bearing', 'bears', 'beast', 'beastality', 'beastiality', 'beat', 'beatles', 'beats', 'beautiful', 'beautifully', 'beauty', 'beaver', 'became', 'because', 'become', 'becomes', 'becoming', 'bed', 'bedding', 'bedford', 'bedroom', 'bedrooms', 'beds', 'bee', 'beef', 'been', 'beer', 'before', 'began', 'begin', 'beginner', 'beginners', 'beginning', 'begins', 'begun', 'behalf', 'behavior', 'behavioral', 'behaviour', 'behind', 'beijing', 'being', 'beings', 'belarus', 'belfast', 'belgium', 'belief', 'beliefs', 'believe', 'believed', 'believes', 'belize', 'belkin', 'bell', 'belle', 'belly', 'belong', 'belongs', 'below', 'belt', 'belts', 'ben', 'bench', 'benchmark', 'bend', 'beneath', 'beneficial', 'benefit', 'benefits', 'benjamin', 'bennett', 'benz', 'berkeley', 'berlin', 'bermuda', 'bernard', 'berry', 'beside', 'besides', 'best', 'bestiality', 'bestsellers', 'bet', 'beta', 'beth', 'better', 'betting', 'betty', 'between', 'beverage', 'beverages', 'beverly', 'beyond', 'bg', 'bhutan', 'bi', 'bias', 'bible', 'biblical', 'bibliographic', 'bibliography', 'bicycle', 'bid', 'bidder', 'bidding', 'bids', 'big', 'bigger', 'biggest', 'bike', 'bikes', 'bikini', 'bill', 'billing', 'billion', 'bills', 'billy', 'bin', 'binary', 'bind', 'binding', 'bingo', 'bio', 'biodiversity', 'biographies', 'biography', 'biol', 'biological', 'biology', 'bios', 'biotechnology', 'bird', 'birds', 'birmingham', 'birth', 'birthday', 'bishop', 'bit', 'bitch', 'bite', 'bits', 'biz', 'bizarre', 'bizrate', 'bk', 'bl', 'black', 'blackberry', 'blackjack', 'blacks', 'blade', 'blades', 'blah', 'blair', 'blake', 'blame', 'blank', 'blanket', 'blast', 'bleeding', 'blend', 'bless', 'blessed', 'blind', 'blink', 'block', 'blocked', 'blocking', 'blocks', 'blog', 'blogger', 'bloggers', 'blogging', 'blogs', 'blond', 'blonde', 'blood', 'bloody', 'bloom', 'bloomberg', 'blow', 'blowing', 'blowjob', 'blowjobs', 'blue', 'blues', 'bluetooth', 'blvd', 'bm', 'bmw', 'bo', 'board', 'boards', 'boat', 'boating', 'boats', 'bob', 'bobby', 'boc', 'bodies', 'body', 'bold', 'bolivia', 'bolt', 'bomb', 'bon', 'bond', 'bondage', 'bonds', 'bone', 'bones', 'bonus', 'boob', 'boobs', 'book', 'booking', 'bookings', 'bookmark', 'bookmarks', 'books', 'bookstore', 'bool', 'boolean', 'boom', 'boost', 'boot', 'booth', 'boots', 'booty', 'border', 'borders', 'bored', 'boring', 'born', 'borough', 'bosnia', 'boss', 'boston', 'both', 'bother', 'botswana', 'bottle', 'bottles', 'bottom', 'bought', 'boulder', 'boulevard', 'bound', 'boundaries', 'boundary', 'bouquet', 'boutique', 'bow', 'bowl', 'bowling', 'box', 'boxed', 'boxes', 'boxing', 'boy', 'boys', 'bp', 'br', 'bra', 'bracelet', 'bracelets', 'bracket', 'brad', 'bradford', 'bradley', 'brain', 'brake', 'brakes', 'branch', 'branches', 'brand', 'brandon', 'brands', 'bras', 'brass', 'brave', 'brazil', 'brazilian', 'breach', 'bread', 'break', 'breakdown', 'breakfast', 'breaking', 'breaks', 'breast', 'breasts', 'breath', 'breathing', 'breed', 'breeding', 'breeds', 'brian', 'brick', 'bridal', 'bride', 'bridge', 'bridges', 'brief', 'briefing', 'briefly', 'briefs', 'bright', 'brighton', 'brilliant', 'bring', 'bringing', 'brings', 'brisbane', 'bristol', 'britain', 'britannica', 'british', 'britney', 'broad', 'broadband', 'broadcast', 'broadcasting', 'broader', 'broadway', 'brochure', 'brochures', 'broke', 'broken', 'broker', 'brokers', 'bronze', 'brook', 'brooklyn', 'brooks', 'bros', 'brother', 'brothers', 'brought', 'brown', 'browse', 'browser', 'browsers', 'browsing', 'bruce', 'brunei', 'brunette', 'brunswick', 'brush', 'brussels', 'brutal', 'bryan', 'bryant', 'bs', 'bt', 'bubble', 'buck', 'bucks', 'budapest', 'buddy', 'budget', 'budgets', 'buf', 'buffalo', 'buffer', 'bufing', 'bug', 'bugs', 'build', 'builder', 'builders', 'building', 'buildings', 'builds', 'built', 'bukkake', 'bulgaria', 'bulgarian', 'bulk', 'bull', 'bullet', 'bulletin', 'bumper', 'bunch', 'bundle', 'bunny', 'burden', 'bureau', 'buried', 'burke', 'burlington', 'burn', 'burner', 'burning', 'burns', 'burst', 'burton', 'bus', 'buses', 'bush', 'business', 'businesses', 'busty', 'busy', 'but', 'butler', 'butt', 'butter', 'butterfly', 'button', 'buttons', 'butts', 'buy', 'buyer', 'buyers', 'buying', 'buys', 'buzz', 'bw', 'by', 'bye', 'byte', 'bytes', 'c', 'ca', 'cab', 'cabin', 'cabinet', 'cabinets', 'cable', 'cables', 'cache', 'cached', 'cad', 'cadillac', 'cafe', 'cage', 'cake', 'cakes', 'cal', 'calcium', 'calculate', 'calculated', 'calculation', 'calculations', 'calculator', 'calculators', 'calendar', 'calendars', 'calgary', 'calibration', 'calif', 'california', 'call', 'called', 'calling', 'calls', 'calm', 'calvin', 'cam', 'cambodia', 'cambridge', 'camcorder', 'camcorders', 'came', 'camel', 'camera', 'cameras', 'cameron', 'cameroon', 'camp', 'campaign', 'campaigns', 'campbell', 'camping', 'camps', 'campus', 'cams', 'can', 'canada', 'canadian', 'canal', 'canberra', 'cancel', 'cancellation', 'cancelled', 'cancer', 'candidate', 'candidates', 'candle', 'candles', 'candy', 'cannon', 'canon', 'cant', 'canvas', 'canyon', 'cap', 'capabilities', 'capability', 'capable', 'capacity', 'cape', 'capital', 'capitol', 'caps', 'captain', 'capture', 'captured', 'car', 'carb', 'carbon', 'card', 'cardiac', 'cardiff', 'cardiovascular', 'cards', 'care', 'career', 'careers', 'careful', 'carefully', 'carey', 'cargo', 'caribbean', 'caring', 'carl', 'carlo', 'carlos', 'carmen', 'carnival', 'carol', 'carolina', 'caroline', 'carpet', 'carried', 'carrier', 'carriers', 'carries', 'carroll', 'carry', 'carrying', 'cars', 'cart', 'carter', 'cartoon', 'cartoons', 'cartridge', 'cartridges', 'cas', 'casa', 'case', 'cases', 'casey', 'cash', 'cashiers', 'casino', 'casinos', 'casio', 'cassette', 'cast', 'casting', 'castle', 'casual', 'cat', 'catalog', 'catalogs', 'catalogue', 'catalyst', 'catch', 'categories', 'category', 'catering', 'cathedral', 'catherine', 'catholic', 'cats', 'cattle', 'caught', 'cause', 'caused', 'causes', 'causing', 'caution', 'cave', 'cayman', 'cb', 'cbs', 'cc', 'ccd', 'cd', 'cdna', 'cds', 'cdt', 'ce', 'cedar', 'ceiling', 'celebrate', 'celebration', 'celebrities', 'celebrity', 'celebs', 'cell', 'cells', 'cellular', 'celtic', 'cement', 'cemetery', 'census', 'cent', 'center', 'centered', 'centers', 'central', 'centre', 'centres', 'cents', 'centuries', 'century', 'ceo', 'ceramic', 'ceremony', 'certain', 'certainly', 'certificate', 'certificates', 'certification', 'certified', 'cest', 'cet', 'cf', 'cfr', 'cg', 'cgi', 'ch', 'chad', 'chain', 'chains', 'chair', 'chairman', 'chairs', 'challenge', 'challenged', 'challenges', 'challenging', 'chamber', 'chambers', 'champagne', 'champion', 'champions', 'championship', 'championships', 'chan', 'chance', 'chancellor', 'chances', 'change', 'changed', 'changelog', 'changes', 'changing', 'channel', 'channels', 'chaos', 'chapel', 'chapter', 'chapters', 'char', 'character', 'characteristic', 'characteristics', 'characterization', 'characterized', 'characters', 'charge', 'charged', 'charger', 'chargers', 'charges', 'charging', 'charitable', 'charity', 'charles', 'charleston', 'charlie', 'charlotte', 'charm', 'charming', 'charms', 'chart', 'charter', 'charts', 'chase', 'chassis', 'chat', 'cheap', 'cheaper', 'cheapest', 'cheat', 'cheats', 'check', 'checked', 'checking', 'checklist', 'checkout', 'checks', 'cheers', 'cheese', 'chef', 'chelsea', 'chem', 'chemical', 'chemicals', 'chemistry', 'chen', 'cheque', 'cherry', 'chess', 'chest', 'chester', 'chevrolet', 'chevy', 'chi', 'chicago', 'chick', 'chicken', 'chicks', 'chief', 'child', 'childhood', 'children', 'childrens', 'chile', 'china', 'chinese', 'chip', 'chips', 'cho', 'chocolate', 'choice', 'choices', 'choir', 'cholesterol', 'choose', 'choosing', 'chorus', 'chose', 'chosen', 'chris', 'christ', 'christian', 'christianity', 'christians', 'christina', 'christine', 'christmas', 'christopher', 'chrome', 'chronic', 'chronicle', 'chronicles', 'chrysler', 'chubby', 'chuck', 'church', 'churches', 'ci', 'cia', 'cialis', 'ciao', 'cigarette', 'cigarettes', 'cincinnati', 'cindy', 'cinema', 'cingular', 'cio', 'cir', 'circle', 'circles', 'circuit', 'circuits', 'circular', 'circulation', 'circumstances', 'circus', 'cisco', 'citation', 'citations', 'cite', 'cited', 'cities', 'citizen', 'citizens', 'citizenship', 'city', 'citysearch', 'civic', 'civil', 'civilian', 'civilization', 'cj', 'cl', 'claim', 'claimed', 'claims', 'claire', 'clan', 'clara', 'clarity', 'clark', 'clarke', 'class', 'classes', 'classic', 'classical', 'classics', 'classification', 'classified', 'classifieds', 'classroom', 'clause', 'clay', 'clean', 'cleaner', 'cleaners', 'cleaning', 'cleanup', 'clear', 'clearance', 'cleared', 'clearing', 'clearly', 'clerk', 'cleveland', 'click', 'clicking', 'clicks', 'client', 'clients', 'cliff', 'climate', 'climb', 'climbing', 'clinic', 'clinical', 'clinics', 'clinton', 'clip', 'clips', 'clock', 'clocks', 'clone', 'close', 'closed', 'closely', 'closer', 'closes', 'closest', 'closing', 'closure', 'cloth', 'clothes', 'clothing', 'cloud', 'clouds', 'cloudy', 'club', 'clubs', 'cluster', 'clusters', 'cm', 'cms', 'cn', 'cnet', 'cnetcom', 'cnn', 'co', 'coach', 'coaches', 'coaching', 'coal', 'coalition', 'coast', 'coastal', 'coat', 'coated', 'coating', 'cock', 'cocks', 'cod', 'code', 'codes', 'coding', 'coffee', 'cognitive', 'cohen', 'coin', 'coins', 'col', 'cold', 'cole', 'coleman', 'colin', 'collaboration', 'collaborative', 'collapse', 'collar', 'colleague', 'colleagues', 'collect', 'collectables', 'collected', 'collectible', 'collectibles', 'collecting', 'collection', 'collections', 'collective', 'collector', 'collectors', 'college', 'colleges', 'collins', 'cologne', 'colombia', 'colon', 'colonial', 'colony', 'color', 'colorado', 'colored', 'colors', 'colour', 'colours', 'columbia', 'columbus', 'column', 'columnists', 'columns', 'com', 'combat', 'combination', 'combinations', 'combine', 'combined', 'combines', 'combining', 'combo', 'come', 'comedy', 'comes', 'comfort', 'comfortable', 'comic', 'comics', 'coming', 'comm', 'command', 'commander', 'commands', 'comment', 'commentary', 'commented', 'comments', 'commerce', 'commercial', 'commission', 'commissioner', 'commissioners', 'commissions', 'commit', 'commitment', 'commitments', 'committed', 'committee', 'committees', 'commodities', 'commodity', 'common', 'commonly', 'commons', 'commonwealth', 'communicate', 'communication', 'communications', 'communist', 'communities', 'community', 'comp', 'compact', 'companies', 'companion', 'company', 'compaq', 'comparable', 'comparative', 'compare', 'compared', 'comparing', 'comparison', 'comparisons', 'compatibility', 'compatible', 'compensation', 'compete', 'competent', 'competing', 'competition', 'competitions', 'competitive', 'competitors', 'compilation', 'compile', 'compiled', 'compiler', 'complaint', 'complaints', 'complement', 'complete', 'completed', 'completely', 'completing', 'completion', 'complex', 'complexity', 'compliance', 'compliant', 'complicated', 'complications', 'complimentary', 'comply', 'component', 'components', 'composed', 'composer', 'composite', 'composition', 'compound', 'compounds', 'comprehensive', 'compressed', 'compression', 'compromise', 'computation', 'computational', 'compute', 'computed', 'computer', 'computers', 'computing', 'con', 'concentrate', 'concentration', 'concentrations', 'concept', 'concepts', 'conceptual', 'concern', 'concerned', 'concerning', 'concerns', 'concert', 'concerts', 'conclude', 'concluded', 'conclusion', 'conclusions', 'concord', 'concrete', 'condition', 'conditional', 'conditioning', 'conditions', 'condo', 'condos', 'conduct', 'conducted', 'conducting', 'conf', 'conference', 'conferences', 'conferencing', 'confidence', 'confident', 'confidential', 'confidentiality', 'config', 'configuration', 'configure', 'configured', 'configuring', 'confirm', 'confirmation', 'confirmed', 'conflict', 'conflicts', 'confused', 'confusion', 'congo', 'congratulations', 'congress', 'congressional', 'conjunction', 'connect', 'connected', 'connecticut', 'connecting', 'connection', 'connections', 'connectivity', 'connector', 'connectors', 'cons', 'conscious', 'consciousness', 'consecutive', 'consensus', 'consent', 'consequence', 'consequences', 'consequently', 'conservation', 'conservative', 'consider', 'considerable', 'consideration', 'considerations', 'considered', 'considering', 'considers', 'consist', 'consistency', 'consistent', 'consistently', 'consisting', 'consists', 'console', 'consoles', 'consolidated', 'consolidation', 'consortium', 'conspiracy', 'const', 'constant', 'constantly', 'constitute', 'constitutes', 'constitution', 'constitutional', 'constraint', 'constraints', 'construct', 'constructed', 'construction', 'consult', 'consultancy', 'consultant', 'consultants', 'consultation', 'consulting', 'consumer', 'consumers', 'consumption', 'contact', 'contacted', 'contacting', 'contacts', 'contain', 'contained', 'container', 'containers', 'containing', 'contains', 'contamination', 'contemporary', 'content', 'contents', 'contest', 'contests', 'context', 'continent', 'continental', 'continually', 'continue', 'continued', 'continues', 'continuing', 'continuity', 'continuous', 'continuously', 'contract', 'contracting', 'contractor', 'contractors', 'contracts', 'contrary', 'contrast', 'contribute', 'contributed', 'contributing', 'contribution', 'contributions', 'contributor', 'contributors', 'control', 'controlled', 'controller', 'controllers', 'controlling', 'controls', 'controversial', 'controversy', 'convenience', 'convenient', 'convention', 'conventional', 'conventions', 'convergence', 'conversation', 'conversations', 'conversion', 'convert', 'converted', 'converter', 'convertible', 'convicted', 'conviction', 'convinced', 'cook', 'cookbook', 'cooked', 'cookie', 'cookies', 'cooking', 'cool', 'cooler', 'cooling', 'cooper', 'cooperation', 'cooperative', 'coordinate', 'coordinated', 'coordinates', 'coordination', 'coordinator', 'cop', 'cope', 'copied', 'copies', 'copper', 'copy', 'copying', 'copyright', 'copyrighted', 'copyrights', 'coral', 'cord', 'cordless', 'core', 'cork', 'corn', 'cornell', 'corner', 'corners', 'cornwall', 'corp', 'corporate', 'corporation', 'corporations', 'corps', 'corpus', 'correct', 'corrected', 'correction', 'corrections', 'correctly', 'correlation', 'correspondence', 'corresponding', 'corruption', 'cos', 'cosmetic', 'cosmetics', 'cost', 'costa', 'costs', 'costume', 'costumes', 'cottage', 'cottages', 'cotton', 'could', 'council', 'councils', 'counsel', 'counseling', 'count', 'counted', 'counter', 'counters', 'counties', 'counting', 'countries', 'country', 'counts', 'county', 'couple', 'coupled', 'couples', 'coupon', 'coupons', 'courage', 'courier', 'course', 'courses', 'court', 'courtesy', 'courts', 'cove', 'cover', 'coverage', 'covered', 'covering', 'covers', 'cow', 'cowboy', 'cox', 'cp', 'cpu', 'cr', 'crack', 'cradle', 'craft', 'crafts', 'craig', 'crap', 'craps', 'crash', 'crawford', 'crazy', 'cream', 'create', 'created', 'creates', 'creating', 'creation', 'creations', 'creative', 'creativity', 'creator', 'creature', 'creatures', 'credit', 'credits', 'creek', 'crest', 'crew', 'cricket', 'crime', 'crimes', 'criminal', 'crisis', 'criteria', 'criterion', 'critical', 'criticism', 'critics', 'crm', 'croatia', 'crop', 'crops', 'cross', 'crossing', 'crossword', 'crowd', 'crown', 'crucial', 'crude', 'cruise', 'cruises', 'cruz', 'cry', 'crystal', 'cs', 'css', 'cst', 'ct', 'cu', 'cuba', 'cube', 'cubic', 'cuisine', 'cult', 'cultural', 'culture', 'cultures', 'cum', 'cumshot', 'cumshots', 'cumulative', 'cunt', 'cup', 'cups', 'cure', 'curious', 'currencies', 'currency', 'current', 'currently', 'curriculum', 'cursor', 'curtis', 'curve', 'curves', 'custody', 'custom', 'customer', 'customers', 'customise', 'customize', 'customized', 'customs', 'cut', 'cute', 'cuts', 'cutting', 'cv', 'cvs', 'cw', 'cyber', 'cycle', 'cycles', 'cycling', 'cylinder', 'cyprus', 'cz', 'czech', 'd', 'da', 'dad', 'daddy', 'daily', 'dairy', 'daisy', 'dakota', 'dale', 'dallas', 'dam', 'damage', 'damaged', 'damages', 'dame', 'damn', 'dan', 'dana', 'dance', 'dancing', 'danger', 'dangerous', 'daniel', 'danish', 'danny', 'dans', 'dare', 'dark', 'darkness', 'darwin', 'das', 'dash', 'dat', 'data', 'database', 'databases', 'date', 'dated', 'dates', 'dating', 'daughter', 'daughters', 'dave', 'david', 'davidson', 'davis', 'dawn', 'day', 'days', 'dayton', 'db', 'dc', 'dd', 'ddr', 'de', 'dead', 'deadline', 'deadly', 'deaf', 'deal', 'dealer', 'dealers', 'dealing', 'deals', 'dealt', 'dealtime', 'dean', 'dear', 'death', 'deaths', 'debate', 'debian', 'deborah', 'debt', 'debug', 'debut', 'dec', 'decade', 'decades', 'december', 'decent', 'decide', 'decided', 'decimal', 'decision', 'decisions', 'deck', 'declaration', 'declare', 'declared', 'decline', 'declined', 'decor', 'decorating', 'decorative', 'decrease', 'decreased', 'dedicated', 'dee', 'deemed', 'deep', 'deeper', 'deeply', 'deer', 'def', 'default', 'defeat', 'defects', 'defence', 'defend', 'defendant', 'defense', 'defensive', 'deferred', 'deficit', 'define', 'defined', 'defines', 'defining', 'definitely', 'definition', 'definitions', 'degree', 'degrees', 'del', 'delaware', 'delay', 'delayed', 'delays', 'delegation', 'delete', 'deleted', 'delhi', 'delicious', 'delight', 'deliver', 'delivered', 'delivering', 'delivers', 'delivery', 'dell', 'delta', 'deluxe', 'dem', 'demand', 'demanding', 'demands', 'demo', 'democracy', 'democrat', 'democratic', 'democrats', 'demographic', 'demonstrate', 'demonstrated', 'demonstrates', 'demonstration', 'den', 'denial', 'denied', 'denmark', 'dennis', 'dense', 'density', 'dental', 'dentists', 'denver', 'deny', 'department', 'departmental', 'departments', 'departure', 'depend', 'dependence', 'dependent', 'depending', 'depends', 'deployment', 'deposit', 'deposits', 'depot', 'depression', 'dept', 'depth', 'deputy', 'der', 'derby', 'derek', 'derived', 'des', 'descending', 'describe', 'described', 'describes', 'describing', 'description', 'descriptions', 'desert', 'deserve', 'design', 'designated', 'designation', 'designed', 'designer', 'designers', 'designing', 'designs', 'desirable', 'desire', 'desired', 'desk', 'desktop', 'desktops', 'desperate', 'despite', 'destination', 'destinations', 'destiny', 'destroy', 'destroyed', 'destruction', 'detail', 'detailed', 'details', 'detect', 'detected', 'detection', 'detective', 'detector', 'determination', 'determine', 'determined', 'determines', 'determining', 'detroit', 'deutsch', 'deutsche', 'deutschland', 'dev', 'devel', 'develop', 'developed', 'developer', 'developers', 'developing', 'development', 'developmental', 'developments', 'develops', 'deviant', 'deviation', 'device', 'devices', 'devil', 'devon', 'devoted', 'df', 'dg', 'dh', 'di', 'diabetes', 'diagnosis', 'diagnostic', 'diagram', 'dial', 'dialog', 'dialogue', 'diameter', 'diamond', 'diamonds', 'diana', 'diane', 'diary', 'dice', 'dick', 'dicke', 'dicks', 'dictionaries', 'dictionary', 'did', 'die', 'died', 'diego', 'dies', 'diesel', 'diet', 'dietary', 'diff', 'differ', 'difference', 'differences', 'different', 'differential', 'differently', 'difficult', 'difficulties', 'difficulty', 'diffs', 'dig', 'digest', 'digit', 'digital', 'dildo', 'dildos', 'dim', 'dimension', 'dimensional', 'dimensions', 'dining', 'dinner', 'dip', 'diploma', 'dir', 'direct', 'directed', 'direction', 'directions', 'directive', 'directly', 'director', 'directories', 'directors', 'directory', 'dirt', 'dirty', 'dis', 'disabilities', 'disability', 'disable', 'disabled', 'disagree', 'disappointed', 'disaster', 'disc', 'discharge', 'disciplinary', 'discipline', 'disciplines', 'disclaimer', 'disclaimers', 'disclose', 'disclosure', 'disco', 'discount', 'discounted', 'discounts', 'discover', 'discovered', 'discovery', 'discrete', 'discretion', 'discrimination', 'discs', 'discuss', 'discussed', 'discusses', 'discussing', 'discussion', 'discussions', 'disease', 'diseases', 'dish', 'dishes', 'disk', 'disks', 'disney', 'disorder', 'disorders', 'dispatch', 'dispatched', 'display', 'displayed', 'displaying', 'displays', 'disposal', 'disposition', 'dispute', 'disputes', 'dist', 'distance', 'distances', 'distant', 'distinct', 'distinction', 'distinguished', 'distribute', 'distributed', 'distribution', 'distributions', 'distributor', 'distributors', 'district', 'districts', 'disturbed', 'div', 'dive', 'diverse', 'diversity', 'divide', 'divided', 'dividend', 'divine', 'diving', 'division', 'divisions', 'divorce', 'divx', 'diy', 'dj', 'dk', 'dl', 'dm', 'dna', 'dns', 'do', 'doc', 'dock', 'docs', 'doctor', 'doctors', 'doctrine', 'document', 'documentary', 'documentation', 'documentcreatetextnode', 'documented', 'documents', 'dod', 'dodge', 'doe', 'does', 'dog', 'dogs', 'doing', 'doll', 'dollar', 'dollars', 'dolls', 'dom', 'domain', 'domains', 'dome', 'domestic', 'dominant', 'dominican', 'don', 'donald', 'donate', 'donated', 'donation', 'donations', 'done', 'donna', 'donor', 'donors', 'dont', 'doom', 'door', 'doors', 'dos', 'dosage', 'dose', 'dot', 'double', 'doubt', 'doug', 'douglas', 'dover', 'dow', 'down', 'download', 'downloadable', 'downloadcom', 'downloaded', 'downloading', 'downloads', 'downtown', 'dozen', 'dozens', 'dp', 'dpi', 'dr', 'draft', 'drag', 'dragon', 'drain', 'drainage', 'drama', 'dramatic', 'dramatically', 'draw', 'drawing', 'drawings', 'drawn', 'draws', 'dream', 'dreams', 'dress', 'dressed', 'dresses', 'dressing', 'drew', 'dried', 'drill', 'drilling', 'drink', 'drinking', 'drinks', 'drive', 'driven', 'driver', 'drivers', 'drives', 'driving', 'drop', 'dropped', 'drops', 'drove', 'drug', 'drugs', 'drum', 'drums', 'drunk', 'dry', 'dryer', 'ds', 'dsc', 'dsl', 'dt', 'dts', 'du', 'dual', 'dubai', 'dublin', 'duck', 'dude', 'due', 'dui', 'duke', 'dumb', 'dump', 'duncan', 'duo', 'duplicate', 'durable', 'duration', 'durham', 'during', 'dust', 'dutch', 'duties', 'duty', 'dv', 'dvd', 'dvds', 'dx', 'dying', 'dylan', 'dynamic', 'dynamics', 'e', 'ea', 'each', 'eagle', 'eagles', 'ear', 'earl', 'earlier', 'earliest', 'early', 'earn', 'earned', 'earning', 'earnings', 'earrings', 'ears', 'earth', 'earthquake', 'ease', 'easier', 'easily', 'east', 'easter', 'eastern', 'easy', 'eat', 'eating', 'eau', 'ebay', 'ebony', 'ebook', 'ebooks', 'ec', 'echo', 'eclipse', 'eco', 'ecological', 'ecology', 'ecommerce', 'economic', 'economics', 'economies', 'economy', 'ecuador', 'ed', 'eddie', 'eden', 'edgar', 'edge', 'edges', 'edinburgh', 'edit', 'edited', 'editing', 'edition', 'editions', 'editor', 'editorial', 'editorials', 'editors', 'edmonton', 'eds', 'edt', 'educated', 'education', 'educational', 'educators', 'edward', 'edwards', 'ee', 'ef', 'effect', 'effective', 'effectively', 'effectiveness', 'effects', 'efficiency', 'efficient', 'efficiently', 'effort', 'efforts', 'eg', 'egg', 'eggs', 'egypt', 'egyptian', 'eh', 'eight', 'either', 'ejaculation', 'el', 'elder', 'elderly', 'elect', 'elected', 'election', 'elections', 'electoral', 'electric', 'electrical', 'electricity', 'electro', 'electron', 'electronic', 'electronics', 'elegant', 'element', 'elementary', 'elements', 'elephant', 'elevation', 'eleven', 'eligibility', 'eligible', 'eliminate', 'elimination', 'elite', 'elizabeth', 'ellen', 'elliott', 'ellis', 'else', 'elsewhere', 'elvis', 'em', 'emacs', 'email', 'emails', 'embassy', 'embedded', 'emerald', 'emergency', 'emerging', 'emily', 'eminem', 'emirates', 'emission', 'emissions', 'emma', 'emotional', 'emotions', 'emperor', 'emphasis', 'empire', 'empirical', 'employ', 'employed', 'employee', 'employees', 'employer', 'employers', 'employment', 'empty', 'en', 'enable', 'enabled', 'enables', 'enabling', 'enb', 'enclosed', 'enclosure', 'encoding', 'encounter', 'encountered', 'encourage', 'encouraged', 'encourages', 'encouraging', 'encryption', 'encyclopedia', 'end', 'endangered', 'ended', 'endif', 'ending', 'endless', 'endorsed', 'endorsement', 'ends', 'enemies', 'enemy', 'energy', 'enforcement', 'eng', 'engage', 'engaged', 'engagement', 'engaging', 'engine', 'engineer', 'engineering', 'engineers', 'engines', 'england', 'english', 'enhance', 'enhanced', 'enhancement', 'enhancements', 'enhancing', 'enjoy', 'enjoyed', 'enjoying', 'enlarge', 'enlargement', 'enormous', 'enough', 'enquiries', 'enquiry', 'enrolled', 'enrollment', 'ensemble', 'ensure', 'ensures', 'ensuring', 'ent', 'enter', 'entered', 'entering', 'enterprise', 'enterprises', 'enters', 'entertaining', 'entertainment', 'entire', 'entirely', 'entities', 'entitled', 'entity', 'entrance', 'entrepreneur', 'entrepreneurs', 'entries', 'entry', 'envelope', 'environment', 'environmental', 'environments', 'enzyme', 'eos', 'ep', 'epa', 'epic', 'epinions', 'epinionscom', 'episode', 'episodes', 'epson', 'eq', 'equal', 'equality', 'equally', 'equation', 'equations', 'equilibrium', 'equipment', 'equipped', 'equity', 'equivalent', 'er', 'era', 'eric', 'ericsson', 'erik', 'erotic', 'erotica', 'erp', 'error', 'errors', 'es', 'escape', 'escort', 'escorts', 'especially', 'espn', 'essay', 'essays', 'essence', 'essential', 'essentially', 'essentials', 'essex', 'est', 'establish', 'established', 'establishing', 'establishment', 'estate', 'estates', 'estimate', 'estimated', 'estimates', 'estimation', 'estonia', 'et', 'etc', 'eternal', 'ethernet', 'ethical', 'ethics', 'ethiopia', 'ethnic', 'eu', 'eugene', 'eur', 'euro', 'europe', 'european', 'euros', 'ev', 'eva', 'eval', 'evaluate', 'evaluated', 'evaluating', 'evaluation', 'evaluations', 'evanescence', 'evans', 'eve', 'even', 'evening', 'event', 'events', 'eventually', 'ever', 'every', 'everybody', 'everyday', 'everyone', 'everything', 'everywhere', 'evidence', 'evident', 'evil', 'evolution', 'ex', 'exact', 'exactly', 'exam', 'examination', 'examinations', 'examine', 'examined', 'examines', 'examining', 'example', 'examples', 'exams', 'exceed', 'excel', 'excellence', 'excellent', 'except', 'exception', 'exceptional', 'exceptions', 'excerpt', 'excess', 'excessive', 'exchange', 'exchanges', 'excited', 'excitement', 'exciting', 'exclude', 'excluded', 'excluding', 'exclusion', 'exclusive', 'exclusively', 'excuse', 'exec', 'execute', 'executed', 'execution', 'executive', 'executives', 'exempt', 'exemption', 'exercise', 'exercises', 'exhaust', 'exhibit', 'exhibition', 'exhibitions', 'exhibits', 'exist', 'existed', 'existence', 'existing', 'exists', 'exit', 'exotic', 'exp', 'expand', 'expanded', 'expanding', 'expansion', 'expansys', 'expect', 'expectations', 'expected', 'expects', 'expedia', 'expenditure', 'expenditures', 'expense', 'expenses', 'expensive', 'experience', 'experienced', 'experiences', 'experiencing', 'experiment', 'experimental', 'experiments', 'expert', 'expertise', 'experts', 'expiration', 'expired', 'expires', 'explain', 'explained', 'explaining', 'explains', 'explanation', 'explicit', 'explicitly', 'exploration', 'explore', 'explorer', 'exploring', 'explosion', 'expo', 'export', 'exports', 'exposed', 'exposure', 'express', 'expressed', 'expression', 'expressions', 'ext', 'extend', 'extended', 'extending', 'extends', 'extension', 'extensions', 'extensive', 'extent', 'exterior', 'external', 'extra', 'extract', 'extraction', 'extraordinary', 'extras', 'extreme', 'extremely', 'eye', 'eyed', 'eyes','robust', 'rochester', 'rock', 'rocket', 'rocks', 'rocky', 'rod', 'roger', 'rogers', 'roland', 'role', 'roles', 'roll', 'rolled', 'roller', 'rolling', 'rolls', 'rom', 'roman', 'romance', 'romania', 'romantic', 'rome', 'ron', 'ronald', 'roof', 'room', 'roommate', 'roommates', 'rooms', 'root', 'roots', 'rope', 'rosa', 'rose', 'roses', 'ross', 'roster', 'rotary', 'rotation', 'rouge', 'rough', 'roughly', 'roulette', 'round', 'rounds', 'route', 'router', 'routers', 'routes', 'routine', 'routines', 'routing', 'rover', 'row', 'rows', 'roy', 'royal', 'royalty', 'rp', 'rpg', 'rpm', 'rr', 'rrp', 'rs', 'rss', 'rt', 'ru', 'rubber', 'ruby', 'rug', 'rugby', 'rugs', 'rule', 'ruled', 'rules', 'ruling', 'run', 'runner', 'running', 'runs', 'runtime', 'rural', 'rush', 'russell', 'russia', 'russian', 'ruth', 'rv', 'rw', 'rwanda', 'rx', 'ryan', 's', 'sa', 'sacramento', 'sacred', 'sacrifice', 'sad', 'saddam', 'safari', 'safe', 'safely', 'safer', 'safety', 'sage', 'sagem', 'said', 'sail', 'sailing', 'saint', 'saints', 'sake', 'salad', 'salaries', 'salary', 'sale', 'salem', 'sales', 'sally', 'salmon', 'salon', 'salt', 'salvador', 'salvation', 'sam', 'samba', 'same', 'samoa', 'sample', 'samples', 'sampling', 'samsung', 'samuel', 'san', 'sand', 'sandra', 'sandwich', 'sandy', 'sans', 'santa', 'sanyo', 'sao', 'sap', 'sapphire', 'sara', 'sarah', 'sas', 'saskatchewan', 'sat', 'satellite', 'satin', 'satisfaction', 'satisfactory', 'satisfied', 'satisfy', 'saturday', 'saturn', 'sauce', 'saudi', 'savage', 'savannah', 'save', 'saved', 'saver', 'saves', 'saving', 'savings', 'saw', 'say', 'saying', 'says', 'sb', 'sbjct', 'sc', 'scale', 'scales', 'scan', 'scanned', 'scanner', 'scanners', 'scanning', 'scary', 'scenario', 'scenarios', 'scene', 'scenes', 'scenic', 'schedule', 'scheduled', 'schedules', 'scheduling', 'schema', 'scheme', 'schemes', 'scholar', 'scholars', 'scholarship', 'scholarships', 'school', 'schools', 'sci', 'science', 'sciences', 'scientific', 'scientist', 'scientists', 'scoop', 'scope', 'score', 'scored', 'scores', 'scoring', 'scotia', 'scotland', 'scott', 'scottish', 'scout', 'scratch', 'screen', 'screening', 'screens', 'screensaver', 'screensavers', 'screenshot', 'screenshots', 'screw', 'script', 'scripting', 'scripts', 'scroll', 'scsi', 'scuba', 'sculpture', 'sd', 'se', 'sea', 'seafood', 'seal', 'sealed', 'sean', 'search', 'searchcom', 'searched', 'searches', 'searching', 'seas', 'season', 'seasonal', 'seasons', 'seat', 'seating', 'seats', 'seattle', 'sec', 'second', 'secondary', 'seconds', 'secret', 'secretariat', 'secretary', 'secrets', 'section', 'sections', 'sector', 'sectors', 'secure', 'secured', 'securely', 'securities', 'security', 'see', 'seed', 'seeds', 'seeing', 'seek', 'seeker', 'seekers', 'seeking', 'seeks', 'seem', 'seemed', 'seems', 'seen', 'sees', 'sega', 'segment', 'segments', 'select', 'selected', 'selecting', 'selection', 'selections', 'selective', 'self', 'sell', 'seller', 'sellers', 'selling', 'sells', 'semester', 'semi', 'semiconductor', 'seminar', 'seminars', 'sen', 'senate', 'senator', 'senators', 'send', 'sender', 'sending', 'sends', 'senegal', 'senior', 'seniors', 'sense', 'sensitive', 'sensitivity', 'sensor', 'sensors', 'sent', 'sentence', 'sentences', 'seo', 'sep', 'separate', 'separated', 'separately', 'separation', 'sept', 'september', 'seq', 'sequence', 'sequences', 'ser', 'serbia', 'serial', 'series', 'serious', 'seriously', 'serum', 'serve', 'served', 'server', 'servers', 'serves', 'service', 'services', 'serving', 'session', 'sessions', 'set', 'sets', 'setting', 'settings', 'settle', 'settled', 'settlement', 'setup', 'seven', 'seventh', 'several', 'severe', 'sewing', 'sex', 'sexcam', 'sexo', 'sexual', 'sexuality', 'sexually', 'sexy', 'sf', 'sg', 'sh', 'shade', 'shades', 'shadow', 'shadows', 'shaft', 'shake', 'shakespeare', 'shakira', 'shall', 'shame', 'shanghai', 'shannon', 'shape', 'shaped', 'shapes', 'share', 'shared', 'shareholders', 'shares', 'shareware', 'sharing', 'shark', 'sharon', 'sharp', 'shaved', 'shaw', 'she', 'shed', 'sheep', 'sheer', 'sheet', 'sheets', 'sheffield', 'shelf', 'shell', 'shelter', 'shemale', 'shemales', 'shepherd', 'sheriff', 'sherman', 'shield', 'shift', 'shine', 'ship', 'shipment', 'shipments', 'shipped', 'shipping', 'ships', 'shirt', 'shirts', 'shit', 'shock', 'shoe', 'shoes', 'shoot', 'shooting', 'shop', 'shopper', 'shoppercom', 'shoppers', 'shopping', 'shoppingcom', 'shops', 'shopzilla', 'shore', 'short', 'shortcuts', 'shorter', 'shortly', 'shorts', 'shot', 'shots', 'should', 'shoulder', 'show', 'showcase', 'showed', 'shower', 'showers', 'showing', 'shown', 'shows', 'showtimes', 'shut', 'shuttle', 'si', 'sic', 'sick', 'side', 'sides', 'sie', 'siemens', 'sierra', 'sig', 'sight', 'sigma', 'sign', 'signal', 'signals', 'signature', 'signatures', 'signed', 'significance', 'significant', 'significantly', 'signing', 'signs', 'signup', 'silence', 'silent', 'silicon', 'silk', 'silly', 'silver', 'sim', 'similar', 'similarly', 'simon', 'simple', 'simplified', 'simply', 'simpson', 'simpsons', 'sims', 'simulation', 'simulations', 'simultaneously', 'sin', 'since', 'sing', 'singapore', 'singer', 'singh', 'singing', 'single', 'singles', 'sink', 'sip', 'sir', 'sister', 'sisters', 'sit', 'site', 'sitemap', 'sites', 'sitting', 'situated', 'situation', 'situations', 'six', 'sixth', 'size', 'sized', 'sizes', 'sk', 'skating', 'ski', 'skiing', 'skill', 'skilled', 'skills', 'skin', 'skins', 'skip', 'skirt', 'skirts', 'sku', 'sky', 'skype', 'sl', 'slave', 'sleep', 'sleeping', 'sleeps', 'sleeve', 'slide', 'slides', 'slideshow', 'slight', 'slightly', 'slim', 'slip', 'slope', 'slot', 'slots', 'slovak', 'slovakia', 'slovenia', 'slow', 'slowly', 'slut', 'sluts', 'sm', 'small', 'smaller', 'smart', 'smell', 'smile', 'smilies', 'smith', 'smithsonian', 'smoke', 'smoking', 'smooth', 'sms', 'smtp', 'sn', 'snake', 'snap', 'snapshot', 'snow', 'snowboard', 'so', 'soa', 'soap', 'soc', 'soccer', 'social', 'societies', 'society', 'sociology', 'socket', 'socks', 'sodium', 'sofa', 'soft', 'softball', 'software', 'soil', 'sol', 'solar', 'solaris', 'sold', 'soldier', 'soldiers', 'sole', 'solely', 'solid', 'solo', 'solomon', 'solution', 'solutions', 'solve', 'solved', 'solving', 'soma', 'somalia', 'some', 'somebody', 'somehow', 'someone', 'somerset', 'something', 'sometimes', 'somewhat', 'somewhere', 'son', 'song', 'songs', 'sonic', 'sons', 'sony', 'soon', 'soonest', 'sophisticated', 'sorry', 'sort', 'sorted', 'sorts', 'sought', 'soul', 'souls', 'sound', 'sounds', 'soundtrack', 'soup', 'source', 'sources', 'south', 'southampton', 'southeast', 'southern', 'southwest', 'soviet', 'sox', 'sp', 'spa', 'space', 'spaces', 'spain', 'spam', 'span', 'spanish', 'spank', 'spanking', 'sparc', 'spare', 'spas', 'spatial', 'speak', 'speaker', 'speakers', 'speaking', 'speaks', 'spears', 'spec', 'special', 'specialist', 'specialists', 'specialized', 'specializing', 'specially', 'specials', 'specialties', 'specialty', 'species', 'specific', 'specifically', 'specification', 'specifications', 'specifics', 'specified', 'specifies', 'specify', 'specs', 'spectacular', 'spectrum', 'speech', 'speeches', 'speed', 'speeds', 'spell', 'spelling', 'spencer', 'spend', 'spending', 'spent', 'sperm', 'sphere', 'spice', 'spider', 'spies', 'spin', 'spine', 'spirit', 'spirits', 'spiritual', 'spirituality', 'split', 'spoke', 'spoken', 'spokesman', 'sponsor', 'sponsored', 'sponsors', 'sponsorship', 'sport', 'sporting', 'sports', 'spot', 'spotlight', 'spots', 'spouse', 'spray', 'spread', 'spreading', 'spring', 'springer', 'springfield', 'springs', 'sprint', 'spy', 'spyware', 'sq', 'sql', 'squad', 'square', 'squirt', 'squirting', 'sr', 'src', 'sri', 'ss', 'ssl', 'st', 'stability', 'stable', 'stack', 'stadium', 'staff', 'staffing', 'stage', 'stages', 'stainless', 'stakeholders', 'stamp', 'stamps', 'stan', 'stand', 'standard', 'standards', 'standing', 'standings', 'stands', 'stanford', 'stanley', 'star', 'starring', 'stars', 'starsmerchant', 'start', 'started', 'starter', 'starting', 'starts', 'startup', 'stat', 'state', 'stated', 'statement', 'statements', 'states', 'statewide', 'static', 'stating', 'station', 'stationery', 'stations', 'statistical', 'statistics', 'stats', 'status', 'statute', 'statutes', 'statutory', 'stay', 'stayed', 'staying', 'stays', 'std', 'ste', 'steady', 'steal', 'steam', 'steel', 'steering', 'stem', 'step', 'stephanie', 'stephen', 'steps', 'stereo', 'sterling', 'steve', 'steven', 'stevens', 'stewart', 'stick', 'sticker', 'stickers', 'sticks', 'sticky', 'still', 'stock', 'stockholm', 'stockings', 'stocks', 'stolen', 'stomach', 'stone', 'stones', 'stood', 'stop', 'stopped', 'stopping', 'stops', 'storage', 'store', 'stored', 'stores', 'stories', 'storm', 'story', 'str', 'straight', 'strain', 'strand', 'strange', 'stranger', 'strap', 'strategic', 'strategies', 'strategy', 'stream', 'streaming', 'streams', 'street', 'streets', 'strength', 'strengthen', 'strengthening', 'strengths', 'stress', 'stretch', 'strict', 'strictly', 'strike', 'strikes', 'striking', 'string', 'strings', 'strip', 'stripes', 'strips', 'stroke', 'strong', 'stronger', 'strongly', 'struck', 'struct', 'structural', 'structure', 'structured', 'structures', 'struggle', 'stuart', 'stuck', 'stud', 'student', 'students', 'studied', 'studies', 'studio', 'studios', 'study', 'studying', 'stuff', 'stuffed', 'stunning', 'stupid', 'style', 'styles', 'stylish', 'stylus', 'su', 'sub', 'subaru', 'subcommittee', 'subdivision', 'subject', 'subjects', 'sublime', 'sublimedirectory', 'submission', 'submissions', 'submit', 'submitted', 'submitting', 'subscribe', 'subscriber', 'subscribers', 'subscription', 'subscriptions', 'subsection', 'subsequent', 'subsequently', 'subsidiaries', 'subsidiary', 'substance', 'substances', 'substantial', 'substantially', 'substitute', 'subtle', 'suburban', 'succeed', 'success', 'successful', 'successfully', 'such', 'suck', 'sucking', 'sucks', 'sudan', 'sudden', 'suddenly', 'sue', 'suffer', 'suffered', 'suffering', 'sufficient', 'sufficiently', 'sugar', 'suggest', 'suggested', 'suggesting', 'suggestion', 'suggestions', 'suggests', 'suicide', 'suit', 'suitable', 'suite', 'suited', 'suites', 'suits', 'sullivan', 'sum', 'summaries', 'summary', 'summer', 'summit', 'sun', 'sunday', 'sunglasses', 'sunny', 'sunrise', 'sunset', 'sunshine', 'super', 'superb', 'superintendent', 'superior', 'supervision', 'supervisor', 'supervisors', 'supplement', 'supplemental', 'supplements', 'supplied', 'supplier', 'suppliers', 'supplies', 'supply', 'support', 'supported', 'supporters', 'supporting', 'supports', 'suppose', 'supposed', 'supreme', 'sur', 'sure', 'surely', 'surf', 'surface', 'surfaces', 'surfing', 'surge', 'surgeon', 'surgeons', 'surgery', 'surgical', 'surname', 'surplus', 'surprise', 'surprised', 'surprising', 'surrey', 'surround', 'surrounded', 'surrounding', 'surveillance', 'survey', 'surveys', 'survival', 'survive', 'survivor', 'survivors', 'susan', 'suse', 'suspect', 'suspected', 'suspended', 'suspension', 'sussex', 'sustainability', 'sustainable', 'sustained', 'suzuki', 'sv', 'sw', 'swap', 'sweden', 'swedish', 'sweet', 'swift', 'swim', 'swimming', 'swing', 'swingers', 'swiss', 'switch', 'switched', 'switches', 'switching', 'switzerland', 'sword', 'sydney', 'symantec', 'symbol', 'symbols', 'sympathy', 'symphony', 'symposium', 'symptoms', 'sync', 'syndicate', 'syndication', 'syndrome', 'synopsis', 'syntax', 'synthesis', 'synthetic', 'syracuse', 'syria', 'sys', 'system', 'systematic', 'systems', 't', 'ta', 'tab', 'table', 'tables', 'tablet', 'tablets', 'tabs', 'tackle', 'tactics', 'tag', 'tagged', 'tags', 'tahoe', 'tail', 'taiwan', 'take', 'taken', 'takes', 'taking', 'tale', 'talent', 'talented', 'tales', 'talk', 'talked', 'talking', 'talks', 'tall', 'tamil', 'tampa', 'tan', 'tank', 'tanks', 'tanzania', 'tap', 'tape', 'tapes', 'tar', 'target', 'targeted', 'targets', 'tariff', 'task', 'tasks', 'taste', 'tattoo', 'taught', 'tax', 'taxation', 'taxes', 'taxi', 'taylor', 'tb', 'tba', 'tc', 'tcp', 'td', 'te', 'tea', 'teach', 'teacher', 'teachers', 'teaches', 'teaching', 'team', 'teams', 'tear', 'tears', 'tech', 'technical', 'technician', 'technique', 'techniques', 'techno', 'technological', 'technologies', 'technology', 'techrepublic', 'ted', 'teddy', 'tee', 'teen', 'teenage', 'teens', 'teeth', 'tel', 'telecharger', 'telecom', 'telecommunications', 'telephone', 'telephony', 'telescope', 'television', 'televisions', 'tell', 'telling', 'tells', 'temp', 'temperature', 'temperatures', 'template', 'templates', 'temple', 'temporal', 'temporarily', 'temporary', 'ten', 'tenant', 'tend', 'tender', 'tennessee', 'tennis', 'tension', 'tent', 'term', 'terminal', 'terminals', 'termination', 'terminology', 'terms', 'terrace', 'terrain', 'terrible', 'territories', 'territory', 'terror', 'terrorism', 'terrorist', 'terrorists', 'terry', 'test', 'testament', 'tested', 'testimonials', 'testimony', 'testing', 'tests', 'tex', 'texas', 'text', 'textbook', 'textbooks', 'textile', 'textiles', 'texts', 'texture', 'tf', 'tft', 'tgp', 'th', 'thai', 'thailand', 'than', 'thank', 'thanks', 'thanksgiving', 'that', 'thats', 'the', 'theater', 'theaters', 'theatre', 'thee', 'theft', 'thehun', 'their', 'them', 'theme', 'themes', 'themselves', 'then', 'theology', 'theorem', 'theoretical', 'theories', 'theory', 'therapeutic', 'therapist', 'therapy', 'there', 'thereafter', 'thereby', 'therefore', 'thereof', 'thermal', 'thesaurus', 'these', 'thesis', 'they', 'thick', 'thickness', 'thin', 'thing', 'things', 'think', 'thinking', 'thinkpad', 'thinks', 'third', 'thirty', 'this', 'thomas', 'thompson', 'thomson', 'thong', 'thongs', 'thorough', 'thoroughly', 'those', 'thou', 'though', 'thought', 'thoughts', 'thousand', 'thousands', 'thread', 'threaded', 'threads', 'threat', 'threatened', 'threatening', 'threats', 'three', 'threesome', 'threshold', 'thriller', 'throat', 'through', 'throughout', 'throw', 'throwing', 'thrown', 'throws', 'thru', 'thu', 'thumb', 'thumbnail', 'thumbnails', 'thumbs', 'thumbzilla', 'thunder', 'thursday', 'thus', 'thy', 'ti', 'ticket', 'tickets', 'tide', 'tie', 'tied', 'tier', 'ties', 'tiffany', 'tiger', 'tigers', 'tight', 'til', 'tile', 'tiles', 'till', 'tim', 'timber', 'time', 'timeline', 'timely', 'timer', 'times', 'timing', 'timothy', 'tin', 'tiny', 'tion', 'tions', 'tip', 'tips', 'tire', 'tired', 'tires', 'tissue', 'tit', 'titanium', 'titans', 'title', 'titled', 'titles', 'tits', 'titten', 'tm', 'tmp', 'tn', 'to', 'tobacco', 'tobago', 'today', 'todd', 'toddler', 'toe', 'together', 'toilet', 'token', 'tokyo', 'told', 'tolerance', 'toll', 'tom', 'tomato', 'tomatoes', 'tommy', 'tomorrow', 'ton', 'tone', 'toner', 'tones', 'tongue', 'tonight', 'tons', 'tony', 'too', 'took', 'tool', 'toolbar', 'toolbox', 'toolkit', 'tools', 'tooth', 'top', 'topic', 'topics', 'topless', 'tops', 'toronto', 'torture', 'toshiba', 'total', 'totally', 'totals', 'touch', 'touched', 'tough', 'tour', 'touring', 'tourism', 'tourist', 'tournament', 'tournaments', 'tours', 'toward', 'towards', 'tower', 'towers', 'town', 'towns', 'township', 'toxic', 'toy', 'toyota', 'toys', 'tp', 'tr', 'trace', 'track', 'trackback', 'trackbacks', 'tracked', 'tracker', 'tracking', 'tracks', 'tract', 'tractor', 'tracy', 'trade', 'trademark', 'trademarks', 'trader', 'trades', 'trading', 'tradition', 'traditional', 'traditions', 'traffic', 'tragedy', 'trail', 'trailer', 'trailers', 'trails', 'train', 'trained', 'trainer', 'trainers', 'training', 'trains', 'tramadol', 'trance', 'tranny', 'trans', 'transaction', 'transactions', 'transcript', 'transcription', 'transcripts', 'transexual', 'transexuales', 'transfer', 'transferred', 'transfers', 'transform', 'transformation', 'transit', 'transition', 'translate', 'translated', 'translation', 'translations', 'translator', 'transmission', 'transmit', 'transmitted', 'transparency', 'transparent', 'transport', 'transportation', 'transsexual', 'trap', 'trash', 'trauma', 'travel', 'traveler', 'travelers', 'traveling', 'traveller', 'travelling', 'travels', 'travesti', 'travis', 'tray', 'treasure', 'treasurer', 'treasures', 'treasury', 'treat', 'treated', 'treating', 'treatment', 'treatments', 'treaty', 'tree', 'trees', 'trek', 'trembl', 'tremendous', 'trend', 'trends', 'treo', 'tri', 'trial', 'trials', 'triangle', 'tribal', 'tribe', 'tribes', 'tribunal', 'tribune', 'tribute', 'trick', 'tricks', 'tried', 'tries', 'trigger', 'trim', 'trinidad', 'trinity', 'trio', 'trip', 'tripadvisor', 'triple', 'trips', 'triumph', 'trivia', 'troops', 'tropical', 'trouble', 'troubleshooting', 'trout', 'troy', 'truck', 'trucks', 'true', 'truly', 'trunk', 'trust', 'trusted', 'trustee', 'trustees', 'trusts', 'truth', 'try', 'trying', 'ts', 'tsunami', 'tt', 'tu', 'tub', 'tube', 'tubes', 'tucson', 'tue', 'tuesday', 'tuition', 'tulsa', 'tumor', 'tune', 'tuner', 'tunes', 'tuning', 'tunisia', 'tunnel', 'turbo', 'turkey', 'turkish', 'turn', 'turned', 'turner', 'turning', 'turns', 'turtle', 'tutorial', 'tutorials', 'tv', 'tvcom', 'tvs', 'twelve', 'twenty', 'twice', 'twiki', 'twin', 'twinks', 'twins', 'twist', 'twisted', 'two', 'tx', 'ty', 'tyler', 'type', 'types', 'typical', 'typically', 'typing', 'u', 'uc', 'uganda', 'ugly', 'uh', 'ui', 'uk', 'ukraine', 'ul', 'ultimate', 'ultimately', 'ultra', 'ultram', 'um', 'un', 'una', 'unable', 'unauthorized', 'unavailable', 'uncertainty', 'uncle', 'und', 'undefined', 'under', 'undergraduate', 'underground', 'underlying', 'understand', 'understanding', 'understood', 'undertake', 'undertaken', 'underwear', 'undo', 'une', 'unemployment', 'unexpected', 'unfortunately', 'uni', 'unified', 'uniform', 'union', 'unions', 'uniprotkb', 'unique', 'unit', 'united', 'units', 'unity', 'univ', 'universal', 'universe', 'universities', 'university', 'unix', 'unknown', 'unless', 'unlike', 'unlikely', 'unlimited', 'unlock', 'unnecessary', 'unsigned', 'unsubscribe', 'until', 'untitled', 'unto', 'unusual', 'unwrap', 'up', 'upc', 'upcoming', 'update', 'updated', 'updates', 'updating', 'upgrade', 'upgrades', 'upgrading', 'upload', 'uploaded', 'upon', 'upper', 'ups', 'upset', 'upskirt', 'upskirts', 'ur', 'urban', 'urge', 'urgent', 'uri', 'url', 'urls', 'uruguay', 'urw', 'us', 'usa', 'usage', 'usb', 'usc', 'usd', 'usda', 'use', 'used', 'useful', 'user', 'username', 'users', 'uses', 'usgs', 'using', 'usps', 'usr', 'usual', 'usually', 'ut', 'utah', 'utc', 'utilities', 'utility', 'utilization', 'utilize', 'utils', 'uv', 'uw', 'uzbekistan', 'v', 'va', 'vacancies', 'vacation', 'vacations', 'vaccine', 'vacuum', 'vagina', 'val', 'valentine', 'valid', 'validation', 'validity', 'valium', 'valley', 'valuable', 'valuation', 'value', 'valued', 'values', 'valve', 'valves', 'vampire', 'van', 'vancouver', 'vanilla', 'var', 'variable', 'variables', 'variance', 'variation', 'variations', 'varied', 'varies', 'variety', 'various', 'vary', 'varying', 'vast', 'vat', 'vatican', 'vault', 'vb', 'vbulletin', 'vc', 'vcr', 've', 'vector', 'vegas', 'vegetable', 'vegetables', 'vegetarian', 'vegetation', 'vehicle', 'vehicles', 'velocity', 'velvet', 'vendor', 'vendors', 'venezuela', 'venice', 'venture', 'ventures', 'venue', 'venues', 'ver', 'verbal', 'verde', 'verification', 'verified', 'verify', 'verizon', 'vermont', 'vernon', 'verse', 'version', 'versions', 'versus', 'vertex', 'vertical', 'very', 'verzeichnis', 'vessel', 'vessels', 'veteran', 'veterans', 'veterinary', 'vg', 'vhs', 'vi', 'via', 'viagra', 'vibrator', 'vibrators', 'vic', 'vice', 'victim', 'victims', 'victor', 'victoria', 'victorian', 'victory', 'vid', 'video', 'videos', 'vids', 'vienna', 'vietnam', 'vietnamese', 'view', 'viewed', 'viewer', 'viewers', 'viewing', 'viewpicture', 'views', 'vii', 'viii', 'viking', 'villa', 'village', 'villages', 'villas', 'vincent', 'vintage', 'vinyl', 'violation', 'violations', 'violence', 'violent', 'violin', 'vip', 'viral', 'virgin', 'virginia', 'virtual', 'virtually', 'virtue', 'virus', 'viruses', 'visa', 'visibility', 'visible', 'vision', 'visit', 'visited', 'visiting', 'visitor', 'visitors', 'visits', 'vista', 'visual', 'vital', 'vitamin', 'vitamins', 'vocabulary', 'vocal', 'vocals', 'vocational', 'voice', 'voices', 'void', 'voip', 'vol', 'volkswagen', 'volleyball', 'volt', 'voltage', 'volume', 'volumes', 'voluntary', 'volunteer', 'volunteers', 'volvo', 'von', 'vote', 'voted', 'voters', 'votes', 'voting', 'voyeur', 'voyeurweb', 'voyuer', 'vp', 'vpn', 'vs', 'vsnet', 'vt', 'vulnerability', 'vulnerable', 'w', 'wa', 'wage', 'wages', 'wagner', 'wagon', 'wait', 'waiting', 'waiver', 'wake', 'wal', 'wales', 'walk', 'walked', 'walker', 'walking', 'walks', 'wall', 'wallace', 'wallet', 'wallpaper', 'wallpapers', 'walls', 'walnut', 'walt', 'walter', 'wan', 'wang', 'wanna', 'want', 'wanted', 'wanting', 'wants', 'war', 'warcraft', 'ward', 'ware', 'warehouse', 'warm', 'warming', 'warned', 'warner', 'warning', 'warnings', 'warrant', 'warranties', 'warranty', 'warren', 'warrior', 'warriors', 'wars', 'was', 'wash', 'washer', 'washing', 'washington', 'waste', 'watch', 'watched', 'watches', 'watching', 'water', 'waterproof', 'waters', 'watershed', 'watson', 'watt', 'watts', 'wav', 'wave', 'waves', 'wax', 'way', 'wayne', 'ways', 'wb', 'wc', 'we', 'weak', 'wealth', 'weapon', 'weapons', 'wear', 'wearing', 'weather', 'web', 'webcam', 'webcams', 'webcast', 'weblog', 'weblogs', 'webmaster', 'webmasters', 'webpage', 'webshots', 'website', 'websites', 'webster', 'wed', 'wedding', 'weddings', 'wednesday', 'weed', 'week', 'weekend', 'weekends', 'weekly', 'weeks', 'weight', 'weighted', 'weights', 'weird', 'welcome', 'welding', 'welfare', 'well', 'wellington', 'wellness', 'wells', 'welsh', 'wendy', 'went', 'were', 'wesley', 'west', 'western', 'westminster', 'wet', 'whale', 'what', 'whatever', 'whats', 'wheat', 'wheel', 'wheels', 'when', 'whenever', 'where', 'whereas', 'wherever', 'whether', 'which', 'while', 'whilst', 'white', 'who', 'whole', 'wholesale', 'whom', 'whore', 'whose', 'why', 'wi', 'wichita', 'wicked', 'wide', 'widely', 'wider', 'widescreen', 'widespread', 'width', 'wife', 'wifi', 'wiki', 'wikipedia', 'wild', 'wilderness', 'wildlife', 'wiley', 'will', 'william', 'williams', 'willing', 'willow', 'wilson', 'win', 'wind', 'window', 'windows', 'winds', 'windsor', 'wine', 'wines', 'wing', 'wings', 'winner', 'winners', 'winning', 'wins', 'winston', 'winter', 'wire', 'wired', 'wireless', 'wires', 'wiring', 'wisconsin', 'wisdom', 'wise', 'wish', 'wishes', 'wishlist', 'wit', 'witch', 'with', 'withdrawal', 'within', 'without', 'witness', 'witnesses', 'wives', 'wizard', 'wm', 'wma', 'wn', 'wolf', 'woman', 'women', 'womens', 'won', 'wonder', 'wonderful', 'wondering', 'wood', 'wooden', 'woods', 'wool', 'worcester', 'word', 'wordpress', 'words', 'work', 'worked', 'worker', 'workers', 'workflow', 'workforce', 'working', 'workout', 'workplace', 'works', 'workshop', 'workshops', 'workstation', 'world', 'worldcat', 'worlds', 'worldsex', 'worldwide', 'worm', 'worn', 'worried', 'worry', 'worse', 'worship', 'worst', 'worth', 'worthy', 'would', 'wound', 'wow', 'wp', 'wr', 'wrap', 'wrapped', 'wrapping', 'wrestling', 'wright', 'wrist', 'write', 'writer', 'writers', 'writes', 'writing', 'writings', 'written', 'wrong', 'wrote', 'ws', 'wt', 'wto', 'wu', 'wv', 'ww', 'www', 'wx', 'wy', 'wyoming', 'x', 'xanax', 'xbox', 'xerox', 'xhtml', 'xi', 'xl', 'xml', 'xnxx', 'xp', 'xx', 'xxx', 'y', 'ya', 'yacht', 'yahoo', 'yale', 'yamaha', 'yang', 'yard', 'yards', 'yarn', 'ye', 'yea', 'yeah', 'year', 'yearly', 'years', 'yeast', 'yellow', 'yemen', 'yen', 'yes', 'yesterday', 'yet', 'yield', 'yields', 'yn', 'yo', 'yoga', 'york', 'yorkshire', 'you', 'young', 'younger', 'your', 'yours', 'yourself', 'youth', 'yr', 'yrs', 'yu', 'yugoslavia', 'yukon', 'z', 'za', 'zambia', 'zdnet', 'zealand', 'zen', 'zero', 'zimbabwe', 'zinc', 'zip', 'zoloft', 'zone', 'zones', 'zoning', 'zoo', 'zoom', 'zoophilia', 'zope', 'zshops', 'zu', 'zum', 'zus',]

def run():
    data()
Teachers_data=[
    ['Sonia','Kapila','12345678','soniakapila@gmail.com'],
    ['Jaspal','Singh','12345678','jaspalsingh@gmail.com'],
    ['Kanta','Devi','12345678','kantadevi@gmail.com'],
    ['Neelam','Seth','12345678','neelamseth@gmail.com']
]
Course_data=[
['MCA',2],
['BTECH CSE',1],
['BCOM',4]
]
Student_data=[
    ['Shuvam','Jaswal','1234567890','shuvamjaswal@gmail.com'],
    ['Vishal','Kumar','1234567890','Vishal@gmail.com'],
    ['Varun','Kumar','1234567890','varunkumar@gmail.com'],
    ['Imran','Ansari','1234567890','imranansari@gmail.com'],
    ['Karun','Beri','1234567890','karunberi@gmail.com'],
    ['Sushrut','Sharma','1234567890','sushrutsharma@gmail.com'],
]

def data():
    users = []
    teachers = []
    students = []
    courses = []
    quizzes = []
    questions = []
    results=[]
    for i in range(0, 4):
        users.append(User.objects.create_user(
            f'{Teachers_data[i][0]}{Teachers_data[i][1]}'.lower(), password=Teachers_data[i][2], email=Teachers_data[i][3], is_teacher=True))
        users[i].first_name = Teachers_data[i][0]
        users[i].last_name = Teachers_data[i][1]
        users[i].save()
    for i in range(0, 6):
        users.append(User.objects.create_user(
            f'{Student_data[i][0]}{Student_data[i][1]}'.lower(), password=Student_data[i][2], email=Student_data[i][3], is_student=True))
        users[i+4].first_name = Student_data[i][0]
        users[i+4].last_name = Student_data[i][1]
        users[i+4].save()
    print(len(users))
    for i in range(0, 3):
        courses.append(Course.objects.create(name=Course_data[i][0], year=Course_data[i][1]))
    for i in range(0, 4):
        teachers.append(Teacher.objects.create(user=users[i]))
    for i in range(4, 10):
        user=users[i]
        course=random.choice(courses)
        students.append(Student.objects.create(
            user=user, course=course))
    Cse_Quiz_data=[
        ['SQL',random.choice(teachers),courses[1]],
        ['Python',random.choice(teachers),courses[1]],
        ['Java',random.choice(teachers),courses[1]]
    ]
    for i in Cse_Quiz_data:
        quizzes.append(Quiz.objects.create(name=f'{i[0]}',author=i[1],course=i[2]))
    Mca_Quiz_data=[
        ['AI',random.choice(teachers),courses[0]],
        ['SQL',random.choice(teachers),courses[0]],
    ]
    for i in Mca_Quiz_data:
        quizzes.append(Quiz.objects.create(name=f'{i[0]}',author=i[1],course=i[2]))
    BCOM_Quiz_data=[
        ['Accounts',random.choice(teachers),courses[2]],
        ['Economics',random.choice(teachers),courses[2]],
    ]
    for i in BCOM_Quiz_data:
        quizzes.append(Quiz.objects.create(name=f'{i[0]}',author=i[1],course=i[2]))
    # for i in range(1,150):
    #     rand_words=[random.choice(words) for i in range(4)]
    #     questions.append(Question.objects.create(quiz=random.choice(quizzes),question=f'Question{i}',A=rand_words[0],B=rand_words[1],C=rand_words[2],D=rand_words[3], answer=random.choice(['A','B','C','D'])))
    Questions_Data=[
        [#SQL
            {'quiz':quizzes[0],
                'question':'What does SQL stand for?',
                'A':'Structured Query Language',
                'B':'Structured Question Language',
                'C':'Strong Question Language',
                'D':'Strong Query Language',
                'answer':'A'},
            {
                'quiz':quizzes[0],
                'question':'Which SQL statement is used to update data in a database?',
                'A':'MODIFY',
                'B':'SAVE AS',
                'C':'UPDATE',
                'D':'SAVE',
                'answer':'C'
            },
            {
                'quiz':quizzes[0],
                'question':'Which SQL statement is used to insert new data in a database?',
                'A':'INSERT NEW',
                'B':'ADD NEW',
                'C':'INSERT INTO',
                'D':'ADD RECORD',
                'answer':'C'
            },
            {
                'quiz':quizzes[0],
                'question':'Which SQL keyword is used to sort the result-set?',
                'A':'ORDER BY',
                'B':'SORT',
                'C':'SORT BY',
                'D':'ORDER',
                'answer':'A'
            },
            {
                'quiz':quizzes[0],
                'question':'What is the most common type of join?',
                'A':'JOINED',
                'B':'INNER JOIN',
                'C':'JOINED TABLE',
                'D':'INSIDE JOIN',
                'answer':'B'
            },
            
        ],
        [#Python
      {
                'quiz':quizzes[1],
                'question':'How do you insert COMMENTS in Python code?',
                'A':'/*This is a comment*/',
                'B':'//This is a comment//',
                'C':'//This is a comment',
                'D':'#This is a comment',
                'answer':'D'
            },
            {
                'quiz':quizzes[1],
                'question':'Which one is NOT a legal variable name?',
                'A':'_myvar',
                'B':'my_var',
                'C':'my-var',
                'D':'myvar',
                'answer':'C'
            },
            {
                'quiz':quizzes[1],
                'question':'What is the correct file extension for Python files?',
                'A':'.pyth',
                'B':',py',
                'C':'.pt',
                'D':'.pyt',
                'answer':'B'
            },
            {
                'quiz':quizzes[1],
                'question':'Which method can be used to remove any whitespace from both the beginning and the end of a string?',
                'A':'ptrim()',
                'B':'strip()',
                'C':'trim()',
                'D':'len()',
                'answer':'B'
            },
            {
                'quiz':quizzes[1],
                'question':'Which method can be used to return a string in upper case letters?',
                'A':'uppercase()',
                'B':'toUpperCase()',
                'C':'upper()',
                'D':'upperCase()',
                'answer':'C'
            },
            
        ],
        [#Java
{
                'quiz':quizzes[2],
                'question':'Which method can be used to find the length of a string?',
                'A':'len()',
                'B':'getSize()',
                'C':'length()',
                'D':'getLength()',
                'answer':'C'
            },
            {
                'quiz':quizzes[2],
                'question':'Which operator can be used to compare two values?',
                'A':'<>',
                'B':'=',
                'C':'==',
                'D':'><',
                'answer':'C'
            },
            {
                'quiz':quizzes[2],
                'question':'To declare an array in Java, define the variable type with:',
                'A':'()',
                'B':'[]',
                'C':'{}',
                'D':'(}',
                'answer':'B'
            },
            {
                'quiz':quizzes[2],
                'question':'Array indexes start with:',
                'A':'1',
                'B':'0',
                'C':'-1',
                'D':'2',
                'answer':'B'
            },
            {
                'quiz':quizzes[2],
                'question':'Which keyword is used to create a class in Java?',
                'A':'MyClass',
                'B':'class',
                'C':'className',
                'D':'class()',
                'answer':'B'
            }
        ],
        [#AI
         {
                'quiz':quizzes[3],
                'question':'Artificial Intelligence is about_____.',
                'A':'Playing a game on Computer',
                'B':'Making a machine Intelligent',
                'C':'Programming on Machine with your Own Intelligence',
                'D':'Putting your intelligence in Machine',
                'answer':'B'
            },
            {
                'quiz':quizzes[3],
                'question':'Who is known as the -Father of AI"?',
                'A':'Fisher Ada',
                'B':'Alan Turing',
                'C':'John McCarthy',
                'D':'Allen Newell',
                'answer':'C'
            },
            {
                'quiz':quizzes[3],
                'question':'Which of the given language is not commonly used for AI?',
                'A':'LISP',
                'B':'PROLOG',
                'C':'Python',
                'D':'Perl',
                'answer':'D'
            },
            {
                'quiz':quizzes[3],
                'question':'The component of an Expert system is_________.',
                'A':'Knowledge Base',
                'B':'Inference Engine',
                'C':'User Interface',
                'D':'All of the above',
                'answer':'D'
            },
            {
                'quiz':quizzes[3],
                'question':'The available ways to solve a problem of state-space-search.',
                'A':'1',
                'B':'2',
                'C':'3',
                'D':'4',
                'answer':'B'
            }
        ],
        [#SQL
            {'quiz':quizzes[4],
                'question':'What does SQL stand for?',
                'A':'Structured Query Language',
                'B':'Structured Question Language',
                'C':'Strong Question Language',
                'D':'Strong Query Language',
                'answer':'A'},
            {
                'quiz':quizzes[4],
                'question':'Which SQL statement is used to update data in a database?',
                'A':'MODIFY',
                'B':'SAVE AS',
                'C':'UPDATE',
                'D':'SAVE',
                'answer':'C'
            },
            {
                'quiz':quizzes[4],
                'question':'Which SQL statement is used to insert new data in a database?',
                'A':'INSERT NEW',
                'B':'ADD NEW',
                'C':'INSERT INTO',
                'D':'ADD RECORD',
                'answer':'C'
            },
            {
                'quiz':quizzes[4],
                'question':'Which SQL keyword is used to sort the result-set?',
                'A':'ORDER BY',
                'B':'SORT',
                'C':'SORT BY',
                'D':'ORDER',
                'answer':'A'
            },
            {
                'quiz':quizzes[4],
                'question':'What is the most common type of join?',
                'A':'JOINED',
                'B':'INNER JOIN',
                'C':'JOINED TABLE',
                'D':'INSIDE JOIN',
                'answer':'B'
            },  
        ],
        [#Accounts
          {
                'quiz':quizzes[5],
                'question':'Which of the following account types increase by debits in double-entry accounting?',
                'A':'Assets, Expenses, Losses',
                'B':'Assets, Revenue, Gains',
                'C':'Expenses, Liabilities, Losses',
                'D':'Gains, Expenses, Liabilities',
                'answer':'A'
            },
            {
                'quiz':quizzes[5],
                'question':'When are liabilities recorded under the accrual basis of accounting?',
                'A':'When incurred',
                'B':'When paid',
                'C':'At the end of the fiscal year',
                'D':'When bank accounts are reconciled',
                'answer':'A'
            },
            {
                'quiz':quizzes[5],
                'question':'Which is not classified as a current asset?',
                'A':'Cash',
                'B':'Product inventory',
                'C':'Prepaid Liabilities',
                'D':'Property',
                'answer':'D'
            },
            {
                'quiz':quizzes[5],
                'question':'What is the minimum number of accounts that accounting entries can have?',
                'A':'1',
                'B':'4',
                'C':'5',
                'D':'2',
                'answer':'D'
            },
            {
                'quiz':quizzes[5],
                'question':'In a journal entry, a debit decreases which of the following accounts?',
                'A':'Cash',
                'B':'Accounts Payable',
                'C':'Supplies Expense',
                'D':'Both A and C',
                'answer':'B'
            },
        ],
        [#Economics
          {
                'quiz':quizzes[6],
                'question':'What do you mean by the supply of goods?',
                'A':'Stock available for sale',
                'B':'Total stock in the warehouse',
                'C':'The actual production of the goods',
                'D':'Quantity of the goods offered for sale at a particular price per unit of time',
                'answer':'D'
            },
            {
                'quiz':quizzes[6],
                'question':'What do you mean by a mixed economy?',
                'A':'Modern and traditional industries',
                'B':'Public and private sectors',
                'C':'Foreign and domestic investments',
                'D':'Commercial and subsistence farming',
                'answer':'B'
            },
            {
                'quiz':quizzes[6],
                'question':'Which of the following is the reason for the decline in the child sex ratio in India?',
                'A':'Low fertility rate',
                'B':'Female foeticide',
                'C':'Incentives for a boy child from the government',
                'D':' None of the above',
                'answer':'B'
            },
            {
                'quiz':quizzes[6],
                'question':'What is the main economic problem faced by the society?',
                'A':'Unemployment',
                'B':'Inequality',
                'C':'Poverty',
                'D':'Scarcity',
                'answer':'D'
            },
            {
                'quiz':quizzes[6],
                'question':'The goal of a pure market economy is to meet the desire of ______ .',
                'A':'Consumers',
                'B':'Companies',
                'C':'Workers',
                'D':'The government',
                'answer':'A'
            },
        ]
    ]
    for subject in Questions_Data:
        for question in subject:
            Question.objects.create(quiz=question['quiz'],question=question['question'],A=question['A'],B=question['B'],C=question['C'],D=question['D'], answer=question['answer'])

    return
    for i in range(1,15):
        all_students=Student.objects.all()
        student=random.choice(all_students)
        course=student.course
        quiz=random.choice(course.quizzes.all())
        a=1
        while Result.objects.filter(student=student,quiz=quiz).exists() and a<10:

            student=random.choice(all_students)
            course=student.course
            quiz=random.choice(course.quizzes.all())
            a+=1
        if a==10:break
        # quiz=random.choice(quizzes)
        # course=quiz.course
        # while (not course.course_students.all()):
        #     quiz=random.choice(quizzes)
        #     course=quiz.course
        #     student=random.choice([i for i in course.course_students.all()])
        #     while(Result.objects.filter(student=student,quiz=quiz)).exists():
        #         student=random.choice([ i for i in course.course_students.all()])
        answer_data={}
        points=0
        # for i in range(0,int((0.5 * len( quiz.questions.all()) +1 ))):
        for i in range(0,len(quiz.questions.all())): 
            if i not in [5,7]:
                answer_data[f'Question {i+1}']=random.choice(['A','B','C','D'])
        for question in quiz.questions.all():
            a = 'Question ' + str(question.question_number)
            if answer_data.get(a)==question.answer:
                points+=1
        results.append(Result.objects.create(student=student,quiz=quiz,answer_data=answer_data,points=points,))
    # user1=User.objects.create_user('user1',password="ilililil",email='abc1@gmail.com',is_teacher=True)
    # user2=User.objects.create_user('user2',password="ilililil",email='abc2@gmail.com',is_teacher=True)
    # user3=User.objects.create_user('user3',password="ilililil",email='abc3@gmail.com',is_teacher=True)
    # user4=User.objects.create_user('user4',password="ilililil",email='abc4@gmail.com',is_student=True)
    # user5=User.objects.create_user('user5',password="ilililil",email='abc5@gmail.com',is_student=True)
    # user6=User.objects.create_user('user6',password="ilililil",email='abc6@gmail.com',is_student=True)
    # teacher1 = Teacher.objects.create(user1)
    # teacher2 = Teacher.objects.create(user2)
    # teacher3 = Teacher.objects.create(user3)
    # student1 = Teacher.objects.create(user=user4)
    # student2 = Teacher.objects.create(user=user5)
    # student3 = Teacher.objects.create(user=user6)
