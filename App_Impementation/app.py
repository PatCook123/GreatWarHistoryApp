from flask import Flask, render_template, request, jsonify
import json
from flask_bootstrap import Bootstrap4
import requests

app = Flask(__name__)
bootstrap = Bootstrap4(app)

nations = {
    "Austria-Hungary": {
        "name": "Austro-Hungarian Empire",
        "date_joined": "July 28th, 1914",
        "alignment": "Central Powers / Triple Alliance",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Flag_of_Austria-Hungary_%281869-1918%29.svg/1280px-Flag_of_Austria-Hungary_%281869-1918%29.svg.png",
        "casualties": "1.7 - 2.1 million dead, 3.6 million wounded",
        "gdp": "$100.5 billion",
        "economy": "Manufacturing and industrial production increased rapidly in the western half of the empire, while the east remained its agricultural heart, producing most of the Dual Monarchy’s food. Austro-Hungary’s annual growth was the second-fastest in Europe, behind that of Germany.",
        "prewar_pop": "50.6 million",
        "mobilized": "7.8 million",
        "allies": "Germany, Bulgaria & the Ottoman Empire",
        "participation": "Austria-Hungary was one the primary belligerents in World War I. In fact, the assassination of Austrian Archduke Franz Ferdinand in 1914 was the primary short-term cause of the war and led to the events of the July Crisis. Austria-Hungary took part in some of the most significant battles of the war on the Italian Front, Eastern, and Balkan Fronts."
    },
    "Germany": {
        "name": "The Germany Empire",
        "date_joined": "August 1st, 1914",
        "alignment": "Central Powers / Triple Alliance",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Flag_of_Germany_%281867%E2%80%931918%29.svg/1280px-Flag_of_Germany_%281867%E2%80%931918%29.svg.png",
        "casualties": "2.2 to 2.8 million dead, 4.2 million wounded",
        "gdp": "$264.3 billion",
        "economy": "Domestically, Germany rode an economic and technological boom for most of the late 1800s. Coal production, iron ore mining and foreign investment all spiked during the mid-19th century. The government adopted policies to encourage industrial growth, while unification removed the border tariffs and trade duties which existed before 1871. German banks formed and grew quickly, providing credit and investment for new ventures. With its large and rapidly growing population (40 million in 1880, 58.5 million by 1910) Germany was able to meet the labour needs of industrialization. By 1900, German steel production exceeded Britain’s and was second only to the United States.",
        "prewar_pop": "67 million",
        "mobilized": "13.2 million",
        "allies": "Austria-Hungary, Bulgaria & the Ottoman Empire",
        "participation": "During most of World War I, the German Empire possessed arguably the most advanced and capable military in the world. It began participation in the conflict after the declaration of war against Serbia by its ally, Austria-Hungary. German forces fought the Allies on both the eastern and western fronts, although German territory itself remained relatively safe from widespread invasion for most of the war, except for a brief period in 1914 when East Prussia was invaded. A tight blockade imposed by the Royal Navy caused severe food shortages in the cities, especially in the winter of 1916–17, known as the Turnip Winter. At the end of the war, Germany's defeat and widespread popular discontent triggered the German Revolution of 1918–1919 which overthrew the monarchy and established the Weimar Republic."
    },
    "Ottoman Empire": {
        "name": "The Ottoman Empire",
        "date_joined": "October 29th, 1914",
        "alignment": "Central Powers / Triple Alliance",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Flag_of_the_Ottoman_Empire_%281844%E2%80%931922%29.svg/1280px-Flag_of_the_Ottoman_Empire_%281844%E2%80%931922%29.svg.png",
        "casualties": "2.8 to 3.3 million dead, 400,000 to 764,000 wounded",
        "gdp": "25.3 billion",
        "economy": "Centuries before, the Ottomans ruled the world’s richest empire – but by the 1800s they had long been overtaken by the trading strength of the British, French and other European powers. By the 1870s the Ottomans owed more than 200 million pounds to European banks; the annual repayments on their loans and interest comprised more than half the national revenue. The Ottoman economy was predominantly agrarian, with agriculture corresponding to 48 percent of the GDP as of 1913. The 19th century had witnessed changes in the structure of land ownership in the Empire. Previously all agricultural lands had belonged to the state and plots were rented to civil servants whose duty was to collect taxes and conscript soldiers. Central government had the total control over economic activities such as production and distribution.",
        "prewar_pop": "23 million",
        "mobilized": "3 million",
        "allies": "Germany, Austria-Hungary & Bulgaria",
        "participation": "The Ottoman Empire fielded an under-equipped and poorly-trained force which fought in the Caucausus, the Middle East, and British Egypt. By the end of the war, the crumbling empire was on its death bed. Its territories were divided between Britan, France, Greece and Russia. In 1922, the empire would officially end with the birth of Turkey as a republic. Turkish forces committed numerous atrocities during the war, including the killing of more than 1.5 million in the Armenian Genocide, still denied by the Turkish government today.."
    },
    "Bulgaria": {
        "name": "The Tsardom of Bulgaria",
        "date_joined": "October 7th, 1915",
        "alignment": "Central Powers / Triple Alliance",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Bulgaria.svg/1920px-Flag_of_Bulgaria.svg.png",
        "casualties": "187,500 killed, 152,390 wounded.",
        "gdp": "$7.4 billion",
        "economy": "Bulgarian participation in the Balkan Wars disrupted the expansion of the Bulgarian economy and proved crippling for public finances, with the financial cost of the war against the Ottoman Empire alone at over 1.3 billion francs. Agriculture, which was the leading sector of the economy, was badly affected, and overall production was reduced by about 9% compared to 1911. Still, the country avoided a large food crisis.[23] Thousands of peasant workers engaged in agricultural activities became casualties during the wars. The number of available horses, sheep, cattle and livestock was between 20% and 40% lower. The single most damaging event was the loss of Southern Dobruja: it had accounted for 20% of Bulgarian grain production before the wars and contained the largest and most developed Bulgarian farming communities.[24] This, combined with bad weather, held the harvest of all crops to 79% of the pre-war level in 1914. Unlike the agriculture sector, Bulgarian industry was less affected, even though problems occurred due to its complete dependence on foreign imports of machinery and spare parts. Production registered a modest decline and was able to maintain a constant level of capital investment that led to recovery of the sector as early as 1914.",
        "prewar_pop": "4.8 million",
        "mobilized": "1.2 million",
        "allies": "Germany, the Austro-Hungarian Empire & the Ottoman Empire",
        "participation": "Bulgaria participated almost solely in the Balkans against Serbia, Romania, and Allied Forces arriving from Salonika, Greece. The kingdom scored major victories against Serbia and helped swiftly defeat Romania."
    },
    "France": {
        "name": "France",
        "date_joined": "August 3rd, 1914",
        "alignment": "Allies / Triple Entente",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%2C_2020%E2%80%93present%29.svg/1920px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%2C_2020%E2%80%93present%29.svg.png",
        "casualties": "1.4 million dead, 4.2 million wounded",
        "gdp": "$137.8 billion",
        "economy": "The 19th century also saw France’s transition from a nation of peasants to a modern and diverse economy. Industrialisation, which had occurred much later in France than in Britain, was nevertheless well underway by the mid-1800s. Thousands of French farmers left their rural villages and relocated to towns and cities, causing rapid urbanisation and its connected problems. By the 1870s, almost one-quarter of French workers were employed in factories and heavy industry. Railway construction was expanded rapidly, furthering internal trade and exports.",
        "prewar_pop": "40 million",
        "mobilized": "8.4 million",
        "allies": "United Kingdom, Russia, Italy, and Serbia",
        "participation": "French forces fought primarily on the Western Front, which occupied much of north-east France. France took part in some of the bloodiest battles of the war including Verdun, the First Battle of the Marne, the Battle of the Frontiers, and the Nivelle Offensive."
    },
    "United Kingdom": {
        "name": "United Kingdom",
        "date_joined": "August 4th, 1914",
        "alignment": "Allies / Triple Entente",
        "flag": "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1920px-Flag_of_the_United_Kingdom.svg.png",
        "casualties": "870,000 to 1.01 million dead, 1.68 million wounded",
        "gdp": "$226.4 billion",
        "economy": "This vast British Empire was, first and foremost, an economic concern. The colonies supplied a wealth of raw materials and products, such as gold and silver, other metals, diamonds, cotton and wool, meat and grain, timber and tea. Britain’s domination of foreign trade was matched by its naval power. The Royal Navy was the world’s largest naval force through the 1800s.",
        "prewar_pop": "46 million",
        "mobilized": "6.2 million",
        "allies": "United Kingdom, Russia, Italy, and Serbia",
        "participation": "The United Kingdom was a leading Allied Power during the First World War of 1914–1918. They fought against the Central Powers, mainly Germany on the Western Front. The armed forces were greatly expanded and reorganised. Additionally, the war marked the founding of the Royal Air Force."
    },
    "Russia": {
        "name": "Russian Empire",
        "date_joined": "July 31st, 1914",
        "alignment": "Allies / Triple Entente",
        "flag": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/1280px-Flag_of_Russia.svg.png",
        "casualties": "2.8 to 3.4 million dead, 3.8 to 4.9 million wounded",
        "gdp": "257.7 billion",
        "economy": "Economically and industrially, the Russian empire lagged well behind the rest of Europe. While the Industrial Revolution had a profound impact on nations like Britain, France and Germany, Russia’s economy remained almost entirely agrarian until the mid-1800s. Industrialisation had also created a raft of new problems in Russia, including urban growth, social disruption, demands for workers’ rights and political agitation. Peasants who relocated to the cities to work in newly opened factories found themselves enduring long working days (often up to 15 hours) in appalling and unsafe conditions, sowing the seeds of revolution among Russia's urban populations.",
        "prewar_pop": "173.2 million",
        "mobilized": "12 million",
        "allies": "France, the United Kingdom, and Serbia",
        "participation": "Russian forces were engaged along the extensive Eastern Front facing German and Austro-Hungarian forces in battles marked by their tremendous casualties and prisoners taken. Additionally, Russian forces would face Ottoman forces in the Caucausus campaign, part of a Russian effort to take advantage of Ottoman weakness obtain previous oil reserves in Ottoman territory. Russia would exit the war in March of 1918 in the wake of the Russian Revolution."
    },
    "Serbia": {
        "name": "Kingdom of Serbia",
        "date_joined": "July 28th, 1914",
        "alignment": "Allies / Triple Entente",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Flag_of_Serbia_%281882%E2%80%931918%29.svg/1280px-Flag_of_Serbia_%281882%E2%80%931918%29.svg.png",
        "casualties": "750,000 to 1.25 million dead, 133,000 wounded.",
        "gdp": "Unknown",
        "economy": "Serbia was an overwhelmingly rural society. It had few mineral or industrial resources and had less than 10,000 people employed in manufacturing. The economy relied heavily on the exports of food to Germany, Turkey and Austria-Hungary.",
        "prewar_pop": "4.5 million",
        "mobilized": "700,000",
        "allies": "France, the United Kingdom, and Russia",
        "participation": "Serbia entered World War I with battle-hardened, outstandingly well-educated officer corps and extremely motivated, well-trained troops, who emerged victorious in two wars only a couple of years before in the last of the Balkan Wars. However, Serbia lacked the industry to properly equip its soldiers and entered the war with only enough modern rifles to equip two-thirds of its forces. Most soldiers did not have up-to-date uniforms and most wore the shoes or boots they brought with them."
    },
    "Italy": {
        "name": "Kingdom of Italy",
        "date_joined": "May 23rd, 1915",
        "alignment": "Allies / Triple Entente",
        "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Italy_%281861-1946%29_crowned.svg/1280px-Flag_of_Italy_%281861-1946%29_crowned.svg.png",
        "casualties": "1 to 1.25 million dead, 950,000 wounded.",
        "gdp": "$91.3 billion",
        "economy": "Italy was still an agrarian economy at the outbreak of the First World War, but did possess a growing industrial base in its northern regions.",
        "prewar_pop": "35.6 million",
        "mobilized": "5.6 million",
        "allies": "United Kingdom, France, Russia and Serbia.",
        "participation": "The Kingdom of Italy joined the war in 1915 after revoking its agreement to a defensive alliance with Germany and Austria-Hungary due to Austria-Hungary's aggression in the Balkans. Italian forces were engaged on the Alpine Front in northern Italy / Southern Austria-Hungary at times fighting on nearly vertical, mountain battlefields. The front was largely static, with 11 battles taking place at the same location in northeastern Italy on the Isonzo River. After a disastrous defeat at the Battle of Caporetto, Italian forces rallied to halt the Austro-Hungarian advance with a victory at Vittorio Veneto, at the base of the Dolomites in northern Italy."
    },
    "United States": {
        "name": "United States of America",
        "date_joined": "April 6th, 1917",
        "alignment": "Allies / Triple Entente",
        "flag": "https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg",
        "casualties": "117,466 dead, 204,002 wounded",
        "gdp": "$511.6 billion",
        "economy": "Prior-to and during the First World War, America was laying the groundwork for its modern capitalist economy. Railroad tracks were laid across the country at astonishing rates, coal mining and steel manufacturing boomed, and technological advances fueled industry, agriculture, and mining. Thousands of new inventions were born in the United States, further fueling the economic boom. The American stock market and American banks benefitted greatly from this economic growth and led to the passing of New York City over London as the world's financial capital.",
        "prewar_pop": "96.5 million",
        "mobilized": "4.3 million",
        "allies": "The United Kingdom, France and Italy",
        "participation": "The United States joined the war in 1917 following the resumption of unrestricted submarine warfare in the Atlantic on American vessels. During this time, German ambassador Arthur Zimmerman send a telegram to his ambassador in Mexico with the instructions of proposing German alliance with Mexico against the United States. Arriving in 1918, American forces would provide much needed manpower and materiel needed to close out the war against Germany on the Western Front. The Americans won a victory at Cantigny, then again in defensive stands at Chateau-Thierry and Belleau Wood. The Americans helped the British Empire, French and Portuguese forces defeat and turn back the powerful final German offensive (Spring Offensive of March to July, 1918), and most importantly, the Americans played a role in the Allied final offensive (Hundred Days Offensive of August to November). However, many American commanders used the same flawed tactics which the British, French, Germans and others had abandoned early in the war, and so many American offensives were not particularly effective. Pershing continued to commit troops to these full-frontal attacks, resulting in high casualties without noticeable military success against experienced veteran German and Austrian-Hungarian units. "
    },
}
sources = ["https://en.wikipedia.org/wiki/United_States_in_World_War_I", "https://spartacus-educational.com/FWWinItaly.htm", "https://royalfamily.org/about-serbia/serbia-in-world-war-i/", "https://www.historycrunch.com/russia-in-world-war-i.html#/", "https://alphahistory.com/worldwar1/ottoman-empire/", "https://en.wikipedia.org/wiki/Bulgaria_during_World_War_I#Economic_situation", "https://www.historycrunch.com/france-in-world-war-i.html#/", "https://alphahistory.com/worldwar1/"]

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/tdih')
def tdih():
    return render_template('tdih.html')

@app.route('/more_info', methods=['POST', 'GET'])
def countries():
    if request.method == 'POST':
        if request.form.get("Select_Nation"):
            nation = request.form["nationDropdown"]
            return render_template('nation_info.j2', nation=nations[nation],
                                   nation_dropdown=nations.keys())

    if request.method == 'GET':
        return render_template('more_info.html', nation_dropdown=nations.keys())


# Sent by calendar input form on TDIH page. Provides month and day,
# receives json object in return containing events on that day from
# microservice.
@app.route('/events', methods=['POST'])
def get_events():
    month = int(request.form['inputMonth'])
    day = int(request.form['inputDay'])
    data = {"month": month, "day": day}
    response = requests.get('http://localhost:5100/events', json=data)
    response = json.loads(response.text)
    response["items"] = len(response["events"])
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)