/* Dữ liệu chèn khi build từ data/*.json */
const DOCS = /*DATA*/[];

/* Dạng câu hỏi và mức độ nhận thức */
const TYPE = {nho:"Ghi nhớ",so:"Phân biệt con số",ss:"So sánh sửa đổi",th:"Tình huống",nd:"Nhiều nhận định",order:"Sắp xếp quy trình",match:"Nối cặp",pb:"Phản biện"};
const LEVEL = {nho:"Ghi nhớ",so:"Ghi nhớ",ss:"Ghi nhớ",th:"Vận dụng",nd:"Vận dụng",order:"Vận dụng",match:"Vận dụng",pb:"Phân tích"};
const LEVELS = ["Ghi nhớ","Vận dụng","Phân tích"];
const KIND = {plus:["Điểm hợp lý","k-plus"],gap:["Cần làm rõ","k-gap"],issue:["Bất cập","k-issue"]};

/* ---------- trạng thái ---------- */
const $ = s => document.querySelector(s);
const store = {
  get(k,d){try{const v=localStorage.getItem("qnhnn:"+k);return v?JSON.parse(v):d}catch(e){return d}},
  set(k,v){try{localStorage.setItem("qnhnn:"+k,JSON.stringify(v))}catch(e){}}
};
let doc = DOCS[0];
let filter = "all", lvl = "all", tyf = "all";
let view = "quiz";
let kindOff = {};
let S = null;
let tick = null;

function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function derange(n){let a;do{a=shuffle([...Array(n).keys()])}while(n>1&&a.every((v,i)=>v===i));return a}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
const L="ABCD";
const kindOf = q => q.k || "mcq";
const tyOf = q => q.ty || "nho";
const fmt = s=>String(Math.floor(s/60)).padStart(2,"0")+":"+String(s%60).padStart(2,"0");

function renderStats(){
  const h = store.get("hist_"+doc.id,[]);
  const best = h.filter(x=>x.mode==="exam").reduce((m,x)=>Math.max(m,Math.round(x.ok/x.n*100)),0);
  const wrong = store.get("wrong_"+doc.id,[]).length;
  $("#stats").innerHTML = `<div><b>${doc.qs.length}</b>câu hỏi</div><div><b>${h.length}</b>lượt làm</div><div><b>${best?best+"%":"–"}</b>điểm thi cao nhất</div><div><b>${wrong}</b>câu cần ôn</div>`;
}
function renderDocs(){
  $("#docs").innerHTML = DOCS.map(d=>`<button class="doc ${d.id===doc.id?"on":""}" type="button" data-id="${d.id}">
    <div class="no">${d.no}</div><div class="tt">${esc(d.title)}</div>
    <div class="meta"><span>Xác thực ngày ${d.date}</span><span>${esc(d.signer)}</span></div></button>
    <div class="chain" style="margin:10px 0 14px">${d.chain.map(c=>`<div><b>${c[0]}</b><br>${c[1]}</div>`).join("")}</div>`).join("");
}

/* ---------- lọc ---------- */
function inChapter(q){ return filter==="all" || (filter==="am" ? !!q.am : q.ch===filter); }
function inLevel(q){ return lvl==="all" || LEVEL[tyOf(q)]===lvl; }
function inType(q){ return tyf==="all" || tyOf(q)===tyf; }
function pool(){ return doc.qs.map((q,i)=>inChapter(q)&&inLevel(q)&&inType(q)?i:-1).filter(i=>i>=0); }

/* ---------- màn hình văn bản ---------- */
function home(){
  clearInterval(tick); S=null;
  const cr = doc.crit;
  const tabs = `<div class="tabs" role="tablist">
    <button type="button" class="tab ${view==="quiz"?"on":""}" data-v="quiz" role="tab">Trắc nghiệm<i>${doc.qs.length}</i></button>
    ${cr?`<button type="button" class="tab ${view==="crit"?"on":""}" data-v="crit" role="tab">Phản biện<i>${cr.items.length}</i></button>`:""}</div>`;
  if(view==="crit" && cr){ critique(tabs, cr); return; }

  const counts = {}; doc.qs.forEach(q=>counts[q.ch]=(counts[q.ch]||0)+1);
  const amCount = doc.qs.filter(q=>q.am).length;
  const wrong = store.get("wrong_"+doc.id,[]);
  const chips = [["all","Tất cả",doc.qs.length],["am",doc.amChip,amCount],...Object.keys(doc.chapters).map(k=>[k,doc.chapters[k].split(" · ")[0],counts[k]||0])];
  const lc = {}; doc.qs.forEach(q=>{const l=LEVEL[tyOf(q)];lc[l]=(lc[l]||0)+1});
  const tc = {}; doc.qs.forEach(q=>{const t=tyOf(q);tc[t]=(tc[t]||0)+1});
  const lchips = [["all","Mọi mức độ",doc.qs.length],...LEVELS.filter(l=>lc[l]).map(l=>[l,l,lc[l]])];
  const tchips = [["all","Mọi dạng",doc.qs.length],...Object.keys(TYPE).filter(t=>tc[t]).map(t=>[t,TYPE[t],tc[t]])];
  const n = pool().length;
  const chipRow = (arr,cur,attr)=>arr.map(c=>`<button type="button" class="chip ${cur===c[0]?"on":""}" data-${attr}="${c[0]}">${c[1]}<i>${c[2]}</i></button>`).join("");
  $("#desk").innerHTML = `
    ${tabs}
    <h2>${esc(doc.title)}</h2>
    <p class="lead">${doc.no} · ${doc.qs.length} câu hỏi, mỗi câu có trích dẫn điều, khoản. Câu có nhãn vàng là ${doc.amLead}.</p>
    <div class="rows" id="filters">
      <div><label class="fl">Phạm vi</label><div class="chips">${chipRow(chips,filter,"f")}</div></div>
      <div><label class="fl">Mức độ</label><div class="chips">${chipRow(lchips,lvl,"l")}</div></div>
      <div><label class="fl">Dạng câu hỏi</label><div class="chips">${chipRow(tchips,tyf,"t")}</div></div>
    </div>
    <label class="fl">Chế độ · ${n} câu khớp bộ lọc</label>
    <div class="modes">
      <button type="button" class="mode" data-m="practice" ${n?"":"disabled"}><span class="k">Luyện tập</span><b>Xem đáp án ngay</b><span>${n?`Làm ${n} câu theo bộ lọc đã chọn, đọc căn cứ sau mỗi câu.`:"Không có câu nào khớp bộ lọc."}</span></button>
      <button type="button" class="mode" data-m="exam"><span class="k">Thi thử</span><b>20 câu · 15 phút</b><span>Trộn mọi dạng câu về nội dung văn bản (trừ phản biện), chấm điểm khi nộp bài. Đạt từ 80%.</span></button>
      <button type="button" class="mode" data-m="wrong" ${wrong.length?"":"disabled"}><span class="k">Ôn câu sai</span><b>${wrong.length} câu</b><span>${wrong.length?"Những câu bạn trả lời sai gần đây.":"Chưa có câu sai nào được lưu."}</span></button>
    </div>
    <h3 class="sec">Cấu trúc văn bản</h3>
    <div class="toc">${Object.keys(doc.chapters).map(k=>{const [a,b]=doc.chapters[k].split(" · ");return `<div><span class="c">${a}</span><span>${b}</span><span class="n">${counts[k]||0} câu</span></div>`}).join("")}</div>
    <p class="note">Nguồn: Văn bản hợp nhất ${doc.no}, đăng trên Cổng Thông tin điện tử Chính phủ. Văn bản hợp nhất dùng để tra cứu; khi áp dụng, ${doc.src}.</p>`;
  bindTabs();
  $("#filters").onclick = e=>{const b=e.target.closest(".chip");if(!b)return;
    if(b.dataset.f!==undefined) filter=b.dataset.f; if(b.dataset.l!==undefined) lvl=b.dataset.l; if(b.dataset.t!==undefined) tyf=b.dataset.t; home()};
  $("#desk").querySelectorAll(".mode").forEach(b=>b.onclick=()=>start(b.dataset.m));
}
function bindTabs(){ $("#desk").querySelectorAll(".tab").forEach(b=>b.onclick=()=>{view=b.dataset.v;home()}); }

function critique(tabs, cr){
  const cnt={}; cr.items.forEach(x=>cnt[x.t]=(cnt[x.t]||0)+1);
  const shown = cr.items.filter(x=>!kindOff[x.t]);
  const pbN = doc.qs.filter(q=>tyOf(q)==="pb").length;
  $("#desk").innerHTML = `
    ${tabs}
    <h2>Phản biện: ${esc(doc.title)}</h2>
    <p class="lead">${doc.no} · Phân tích điểm hợp lý, điểm cần làm rõ và bất cập, kèm căn cứ điều khoản và hướng hoàn thiện.</p>
    <p class="crit-sum">${esc(cr.sum)}</p>
    ${pbN?`<div class="nav" style="margin:0 0 20px;justify-content:flex-start"><button type="button" class="btn" id="pbgo">Làm quiz phản biện · ${pbN} câu</button></div>`:""}
    <div class="legend">${Object.keys(KIND).map(k=>`<button type="button" class="pill ${KIND[k][1]} ${kindOff[k]?"off":""}" data-k="${k}" aria-pressed="${!kindOff[k]}">${KIND[k][0]} · ${cnt[k]||0}</button>`).join("")}</div>
    <div class="crits">${shown.map(x=>`<article class="crit">
      <span class="kind ${KIND[x.t][1]}">${KIND[x.t][0]}</span>
      <div class="ch"><b>${esc(x.title)}</b><span>${esc(x.cite)}</span></div>
      <p>${esc(x.body)}</p>
      ${x.rec?`<div class="rec"><b>Hướng hoàn thiện</b>${esc(x.rec)}</div>`:""}
    </article>`).join("") || `<p class="lead">Bật lại ít nhất một nhóm ở trên để xem nội dung.</p>`}</div>
    <h3 class="sec" style="margin-top:26px">Câu hỏi thảo luận</h3>
    <ol class="disc">${cr.discuss.map(d=>`<li>${esc(d)}</li>`).join("")}</ol>
    <p class="note">Phần phản biện là phân tích mang tính học thuật, soạn dựa trên nội dung văn bản hợp nhất để phục vụ ôn tập và thảo luận. Đây không phải quan điểm chính thức của Ngân hàng Nhà nước hay cơ quan ban hành.</p>`;
  bindTabs();
  if($("#pbgo")) $("#pbgo").onclick=()=>{view="quiz";filter="all";lvl="all";tyf="pb";start("practice")};
  $("#desk").querySelectorAll(".pill").forEach(b=>b.onclick=()=>{kindOff[b.dataset.k]=!kindOff[b.dataset.k];home()});
}

/* ---------- phiên làm bài ---------- */
function start(mode){
  let ids;
  if(mode==="wrong") ids = shuffle(store.get("wrong_"+doc.id,[]).filter(i=>doc.qs[i]));
  else if(mode==="exam") ids = shuffle(doc.qs.map((q,i)=>tyOf(q)==="pb"?-1:i).filter(i=>i>=0)).slice(0,20);
  else ids = pool();
  if(!ids.length) return;
  S = {mode, ids, i:0, ans:{}, order:{}, st:{}, mo:{}, t0:Date.now(), limit: mode==="exam"?15*60:0, done:false};
  ids.forEach(id=>{const q=doc.qs[id],k=kindOf(q);
    if(k==="mcq") S.order[id]=shuffle([0,1,2,3]);
    else if(k==="order") S.st[id]=derange(q.items.length);
    else if(k==="match"){ S.mo[id]=derange(q.pairs.length); S.st[id]=q.pairs.map(()=>-1); }
  });
  clearInterval(tick);
  if(S.limit){tick=setInterval(()=>{const el=$("#timer");if(!el||!S)return;const left=S.limit-Math.floor((Date.now()-S.t0)/1000);if(left<=0){finish();return}el.textContent=fmt(left);el.classList.toggle("low",left<120)},1000)}
  question();
  if(window.innerWidth<860){ try{ $("#desk").scrollIntoView({block:"start"}); }catch(e){} }
}

/* Chấm câu sắp xếp và nối cặp */
function judge(id){
  const q=doc.qs[id], st=S.st[id];
  if(kindOf(q)==="order") return st.every((v,i)=>v===i);
  return st.every((v,i)=>v===i);
}
function answerText(q,id,mine){
  const k=kindOf(q);
  if(k==="mcq") return mine ? (S.ans[id]===undefined?null:q.o[S.ans[id]]) : q.o[0];
  if(k==="order") return mine ? S.st[id].map(i=>q.items[i]).join(" → ") : q.items.join(" → ");
  return mine ? q.pairs.map((p,i)=>`${p[0]} → ${S.st[id][i]>=0?q.pairs[S.st[id][i]][1]:"(bỏ trống)"}`).join("; ")
              : q.pairs.map(p=>`${p[0]} → ${p[1]}`).join("; ");
}

function question(){
  const id=S.ids[S.i], q=doc.qs[id], k=kindOf(q), picked=S.ans[id];
  const reveal = S.mode!=="exam" && picked!==undefined;
  const label = {practice:"Luyện tập",exam:"Thi thử",wrong:"Ôn câu sai"}[S.mode];
  const answered = Object.keys(S.ans).length;
  const t = tyOf(q);
  let body = "";
  if(k==="mcq"){
    const ord=S.order[id];
    body = `<div class="opts">${ord.map((oi,j)=>{
      let cls=""; if(reveal){ if(oi===0) cls="ok"; else if(oi===picked) cls="bad"; } else if(picked===oi) cls="pick";
      return `<button type="button" class="opt ${cls}" data-o="${oi}" ${reveal?"disabled":""}><span class="l">${L[j]}</span><span>${esc(q.o[oi])}</span></button>`}).join("")}</div>`;
  } else if(k==="order"){
    const st=S.st[id];
    body = `<p class="hint">Dùng nút ↑ ↓ để đưa các bước về đúng thứ tự.</p><ol class="ord">${st.map((it,pos)=>{
      let cls=""; if(reveal) cls = it===pos?"ok":"bad";
      return `<li class="${cls}"><span class="n">${pos+1}</span><span>${esc(q.items[it])}</span>
        <span class="mv"><button type="button" data-up="${pos}" aria-label="Đưa lên" ${reveal||pos===0?"disabled":""}>↑</button><button type="button" data-dn="${pos}" aria-label="Đưa xuống" ${reveal||pos===st.length-1?"disabled":""}>↓</button></span>
        ${reveal&&it!==pos?`<span class="fix">Đúng ở vị trí này: ${esc(q.items[pos])}</span>`:""}</li>`}).join("")}</ol>`;
  } else {
    const st=S.st[id], mo=S.mo[id];
    body = `<p class="hint">Chọn nội dung tương ứng cho từng dòng bên trái.</p><div class="mt">${q.pairs.map((p,i)=>{
      let cls=""; if(reveal) cls = st[i]===i?"ok":"bad";
      return `<div class="row ${cls}"><span class="l">${esc(p[0])}</span>
        <select id="m-${id}-${i}" data-i="${i}" ${reveal?"disabled":""} aria-label="${esc(p[0])}"><option value="-1">Chọn…</option>${mo.map(r=>`<option value="${r}" ${st[i]===r?"selected":""}>${esc(q.pairs[r][1])}</option>`).join("")}</select>
        ${reveal&&st[i]!==i?`<span class="fix">Đáp án đúng: ${esc(p[1])}</span>`:""}</div>`}).join("")}</div>`;
  }
  const canCheck = k!=="mcq" && S.mode!=="exam" && !reveal;
  const ready = k==="match" ? S.st[id].every(v=>v>=0) : true;
  $("#desk").innerHTML = `
    <div class="bar"><span>${label} · Câu ${S.i+1}/${S.ids.length}</span>
      <span>${S.limit?`Còn lại <span class="timer" id="timer">${fmt(Math.max(0,S.limit-Math.floor((Date.now()-S.t0)/1000)))}</span> · `:""}Đã trả lời ${answered}</span></div>
    <div class="prog"><i style="width:${(S.i+1)/S.ids.length*100}%"></i></div>
    <div class="qtag"><span class="tag">${doc.chapters[q.ch].split(" · ")[0]}</span>${t!=="nho"&&t!=="pb"?`<span class="tag ty">${TYPE[t]}</span>`:""}<span class="tag ty">${LEVEL[t]}</span>${q.am?`<span class="tag am">${typeof q.am==="string"?q.am:doc.amTag}</span>`:""}</div>
    ${q.sc?`<div class="case"><b>Tình huống</b>${esc(q.sc)}</div>`:""}
    <p class="q">${esc(q.q)}</p>
    ${q.st?`<ol class="stmts">${q.st.map(s=>`<li><span>${esc(s)}</span></li>`).join("")}</ol>`:""}
    ${body}
    ${reveal?`<div class="basis"><div class="hd ${picked===0?"ok":"bad"}">${picked===0?"Chính xác":(k==="mcq"?"Chưa đúng · Đáp án "+L[S.order[id].indexOf(0)]:"Chưa đúng · Xem phần sửa ở trên")}<span>${esc(q.c)}</span></div><blockquote>${esc(q.ex)}</blockquote></div>`:""}
    <div class="nav">
      <button type="button" class="btn quiet" id="quit">Thoát</button>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        ${canCheck?`<button type="button" class="btn ghost" id="check" ${ready?"":"disabled"}>Kiểm tra</button>`:""}
        <button type="button" class="btn ghost" id="prev" ${S.i===0?"disabled":""}>Câu trước</button>
        ${S.i<S.ids.length-1?`<button type="button" class="btn" id="next">Câu tiếp</button>`:`<button type="button" class="btn" id="end">${S.mode==="exam"?"Nộp bài":"Xem kết quả"}</button>`}
      </div>
    </div>`;
  const touch = ()=>{ if(S.mode==="exam") S.ans[id]="x"; };
  $("#desk").querySelectorAll(".opt").forEach(b=>b.onclick=()=>{
    if(S.mode!=="exam" && S.ans[id]!==undefined) return;
    S.ans[id]=+b.dataset.o; question();
  });
  $("#desk").querySelectorAll("[data-up],[data-dn]").forEach(b=>b.onclick=()=>{
    const st=S.st[id]; const p=+(b.dataset.up??b.dataset.dn); const j=b.dataset.up!==undefined?p-1:p+1;
    [st[p],st[j]]=[st[j],st[p]]; touch(); question();
    const f=$(`[data-${b.dataset.up!==undefined?"up":"dn"}="${j}"]`); if(f&&!f.disabled) f.focus();
  });
  $("#desk").querySelectorAll(".mt select").forEach(sel=>sel.onchange=()=>{
    S.st[id][+sel.dataset.i]=+sel.value; touch(); question();
    const f=document.getElementById(sel.id); if(f) f.focus();
  });
  if($("#check")) $("#check").onclick=()=>{ S.ans[id]=judge(id)?0:1; question(); };
  $("#quit").onclick=home;
  $("#prev").onclick=()=>{S.i--;question()};
  if($("#next")) $("#next").onclick=()=>{S.i++;question()};
  if($("#end")) $("#end").onclick=finish;
}

function finish(){
  if(!S||S.done) return; S.done=true; clearInterval(tick);
  // chấm các câu sắp xếp / nối cặp đã thao tác trong chế độ thi
  S.ids.forEach(id=>{ if(S.ans[id]==="x") S.ans[id]=judge(id)?0:1; });
  const n=S.ids.length, ok=S.ids.filter(id=>S.ans[id]===0).length;
  const pct=Math.round(ok/n*100), secs=Math.floor((Date.now()-S.t0)/1000);
  let wrong=new Set(store.get("wrong_"+doc.id,[]));
  S.ids.forEach(id=>{ if(S.ans[id]===0) wrong.delete(id); else if(S.ans[id]!==undefined) wrong.add(id); });
  store.set("wrong_"+doc.id,[...wrong]);
  const h=store.get("hist_"+doc.id,[]); h.push({mode:S.mode,n,ok,at:Date.now()}); store.set("hist_"+doc.id,h.slice(-50));
  renderStats();
  const by={}; S.ids.forEach(id=>{const l=LEVEL[tyOf(doc.qs[id])];by[l]=by[l]||{n:0,ok:0};by[l].n++;if(S.ans[id]===0)by[l].ok++});
  const byc={}; S.ids.forEach(id=>{const c=doc.qs[id].ch;byc[c]=byc[c]||{n:0,ok:0};byc[c].n++;if(S.ans[id]===0)byc[c].ok++});
  const miss=S.ids.filter(id=>S.ans[id]!==0);
  const pass=pct>=80;
  const d=new Date();
  const bars=(o,name)=>Object.keys(o).map(c=>`<div><span>${name(c)}</span><span class="m"><i style="width:${o[c].ok/o[c].n*100}%"></i></span><span class="v">${o[c].ok}/${o[c].n}</span></div>`).join("");
  $("#desk").innerHTML = `
    <div class="seal">
      <div class="sh"><span>Giấy niêm phong · Kết quả kiểm đếm</span><span>${doc.no}</span></div>
      <span class="stamp">${pass?"ĐẠT":"CHƯA ĐẠT"}</span>
      <dl>
        <div><dt>Ngày kiểm đếm</dt><dd>${String(d.getDate()).padStart(2,"0")}/${String(d.getMonth()+1).padStart(2,"0")}/${d.getFullYear()}</dd></div>
        <div><dt>Số câu (tờ)</dt><dd>${n}</dd></div>
        <div><dt>Đúng</dt><dd>${ok}</dd></div>
        <div><dt>Tỷ lệ</dt><dd>${pct}%</dd></div>
        <div><dt>Thời gian</dt><dd>${fmt(secs)}</dd></div>
      </dl>
      <div class="verdict">${pass?"Bạn nắm vững nội dung trong phạm vi này.":"Ngưỡng đạt là 80%. Xem lại các câu sai bên dưới, chúng đã được lưu vào mục Ôn câu sai."}</div>
    </div>
    <h3 class="sec">Theo mức độ</h3>
    <div class="brk">${bars(by,x=>x)}</div>
    <h3 class="sec">Theo chương</h3>
    <div class="brk">${bars(byc,c=>doc.chapters[c])}</div>
    ${miss.length?`<h3 class="sec">Câu cần xem lại (${miss.length})</h3><div class="rev">${miss.map(id=>{const q=doc.qs[id],mine=S.ans[id]===undefined?null:answerText(q,id,true);return `<article><div class="rq">${q.sc?esc(q.sc)+" ":""}${esc(q.q)}</div>${q.st?`<div class="ra">${q.st.map((s,i)=>`<span>(${i+1}) ${esc(s)}</span>`).join("")}</div>`:""}<div class="ra">${mine===null?`<span class="y">Bỏ trống</span>`:`<span class="y">Bạn chọn: ${esc(mine)}</span>`}<span class="r">Đáp án: ${esc(answerText(q,id,false))}</span></div><div class="rc">${esc(q.c)} · “${esc(q.ex)}”</div></article>`}).join("")}</div>`:""}
    <div class="nav"><button type="button" class="btn quiet" id="back">Về trang văn bản</button><button type="button" class="btn" id="again">Làm lại</button></div>`;
  const m=S.mode;
  $("#back").onclick=home; $("#again").onclick=()=>start(m==="wrong"&&!store.get("wrong_"+doc.id,[]).length?"practice":m);
}

$("#docs").addEventListener("click",e=>{const b=e.target.closest(".doc[data-id]");if(!b)return;doc=DOCS.find(d=>d.id===b.dataset.id);filter="all";lvl="all";tyf="all";kindOff={};renderDocs();renderStats();home()});
renderDocs(); renderStats(); home();
